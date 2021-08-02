from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import requests
from redis import Redis
from rq import Queue
from updater import update_product
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/ordenes.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)
api = Api(app)

token = requests.get(f"https://jwt-queries:5000/api-queries/jwt", verify=False)
token = token.json()
headers = {'Authorization': f"Bearer {token['access_token']}"}
queue_name = None
try:
    queue_name = requests.get(f"https://acl-queries:5000/api-queries/acl/orders/q", verify=False, headers=headers)
    queue_name = queue_name.json()
    queue_name = queue_name['value']
except:
    print("Queue q not in ACL for Service orders")
    exit(1)

q = Queue(connection=Redis(host='redis', port=6379, db=queue_name))
queue_name = None
try:
    queue_name = requests.get(f"https://acl-queries:5000/api-queries/acl/orders/q2", verify=False, headers=headers)
    queue_name = queue_name.json()
    queue_name = queue_name['value']
except:
    print("Queue q2 not in ACL for Service orders")
    exit(1)

q2 = Queue(connection=Redis(host='redis', port=6379, db=queue_name))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    product = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    state = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    value = db.Column(db.Integer)
    stock = db.Column(db.Integer)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "user", "prodcut", "quantity", "state")


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

def process_order(order_id):
    order = Order.query.get(order_id)
    product = Product.query.get(order.product)
    if product.stock >= order.quantity:
        product.stock = product.stock-order.quantity
        q2.enqueue(update_product, {
            'id': product.id,
            'quantity': order.quantity
        })
        order.state = "completed"
    else:
        order.state = "failed"
    db.session.commit()