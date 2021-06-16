from base import db, Product
def update_product(data):
    product = Product.query.get(data['id'])
    product.stock = product.stock - data['quantity']
    db.session.commit()