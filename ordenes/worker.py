from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import requests
from redis import Redis
from rq import Queue


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/ordenes.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
q = Queue(connection=Redis(host='redis', port=6379, db=0))

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
    product = requests.get(f"http://products:5000/products/{order.product}")
    product = product.json()
    if product['stock'] >= order.quantity:
        requests.put(f"http://products:5000/products/{order.product}", json={'stock': product['stock']-order.quantity})
        order.state = "completed"
    else:
        order.state = "failed"
    db.session.commit()