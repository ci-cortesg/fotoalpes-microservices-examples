from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import requests
from redis import Redis
from rq import Queue
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/ordenes.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)
api = Api(app)

token = requests.get(f"https://jwt:5000/jwt", verify=False)
token = token.json()
headers = {'Authorization': f"Bearer {token['access_token']}"}
queue_name = None
try:
    queue_name = requests.get(f"https://acl:5000/acl/orders/orders", verify=False, headers=headers)
    queue_name = queue_name.json()
    queue_name = queue_name['id']
except:
    print("Queue not in ACL for this Service")
    exit(1)

q = Queue(connection=Redis(host='redis', port=6379, db=queue_name))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    product = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    state = db.Column(db.String(100))


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "user", "prodcut", "quantity", "state")


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

def process_order(order_id):
    order = Order.query.get(order_id)
    token = requests.get(f"https://jwt:5000/jwt", verify=False)
    token = token.json()
    headers = {'Authorization': f"Bearer {token['access_token']}"}
    product = requests.get(f"https://products:5000/products/{order.product}", verify=False, headers=headers)
    product = product.json()
    if product['stock'] >= order.quantity:
        requests.put(f"https://products:5000/products/{order.product}", json={'stock': product['stock']-order.quantity}, verify=False, headers=headers)
        order.state = "completed"
    else:
        order.state = "failed"
    db.session.commit()