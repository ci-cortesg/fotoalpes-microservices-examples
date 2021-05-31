from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/productos.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


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


class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return products_schema.dump(products)

    def post(self):
        new_product = Product(
            name=request.json['name'],
            description=request.json['description'],
            value=request.json['value'],
            stock=request.json['stock'],
        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product)


class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return user_schema.dump(product)
    
    def put(self, product_id):
        product = Product.query.get_or_404(product_id)
        if 'name' in request.json:
            product.name = request.json['name']
        if 'description' in request.json:
            product.description = request.json['description']
        if 'value' in request.json:
            product.value = request.json['value']
        if 'stock' in request.json:
            product.stock = request.json['stock']
        db.session.commit()
        return product_schema.dump(product)




api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:product_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')