from base import app, api, ma, db, Product, product_schema, products_schema, q, Resource, Flask, request
from sender import send_product


class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return products_schema.dump(products)

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)


api.add_resource(ProductListResource, '/api-queries/products')
api.add_resource(ProductResource, '/api-queries/products/<int:product_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')