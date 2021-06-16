from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from redis import Redis
from rq import Queue
from sender import send_product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/productos.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

q = Queue(connection=Redis(host='redis', port=6379, db=0))


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