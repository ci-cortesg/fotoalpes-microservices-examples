from base import db, Product

def put_product(data):
    product = Product.query.get(data['id'])
    product.stock = data['stock']
    product.description = data['description']
    product.value = data['value']
    db.session.commit()