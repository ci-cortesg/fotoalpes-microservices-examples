from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/ordenes.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    value = db.Column(db.Integer)
    stock = db.Column(db.Integer)

def send_product(product_data):
    product = Product(
            id=product_data['id'],
            name=product_data['name'],
            description=product_data['description'],
            value=product_data['value'],
            stock=product_data['stock'],
        )
    db.session.add(product)
    db.session.commit()