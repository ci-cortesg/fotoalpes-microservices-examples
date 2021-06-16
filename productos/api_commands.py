from base import app, api, ma, db, Product, product_schema, products_schema, q, Resource, Flask, request
from sender import send_product
from putter import put_product


class ProductListResource(Resource):

    def post(self):
        new_product = Product(
            name=request.json['name'],
            description=request.json['description'],
            value=request.json['value'],
            stock=request.json['stock'],
        )
        db.session.add(new_product)
        db.session.commit()
        q.enqueue(send_product, product_schema.dump(new_product))
        return product_schema.dump(new_product)

class ProductResource(Resource):
    
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
        q.enqueue(put_product, product_schema.dump(product))
        return product_schema.dump(product)




api.add_resource(ProductListResource, '/api-commands/products')
api.add_resource(ProductResource, '/api-commands/products/<int:product_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')