from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from redis import Redis
from rq import Queue
import requests
from sender import send_product
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/productos.db'
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
    queue_name = requests.get(f"https://acl-queries:5000/api-queries/acl/products/q", verify=False, headers=headers)
    queue_name = queue_name.json()
    queue_name = queue_name['value']
except:
    print("Queue q not in ACL for Service products")
    exit(1)

q = Queue(connection=Redis(host='redis', port=6379, db=queue_name))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    value = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "name", "description", "value", "stock")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)