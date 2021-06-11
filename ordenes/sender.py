from base import Product, User, db

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


def send_user(user_data):
    user = User(
            id=user_data['id'],
            username=user_data['username'],
        )
    db.session.add(user)
    db.session.commit()