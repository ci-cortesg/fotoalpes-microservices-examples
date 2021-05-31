from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import requests
import pika


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/ordenes.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


def sent_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()

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


class OrderListResource(Resource):
    def get(self):
        orders = Order.query.all()
        return orders_schema.dump(orders)

    def post(self):
        user = requests.get(f"http://users:5000/users/{request.json['user']}")
        product = requests.get(f"http://products:5000/products/{request.json['product']}")
        if user.status_code==200 and product.status_code==200:
            new_order = Order(
                user=request.json['user'],
                product=request.json['product'],
                quantity=request.json['quantity'],
                state="processing",
            )
            db.session.add(new_order)
            db.session.commit()
            # add to queue to process order
            sent_message(str(new_order.id))
            return order_schema.dump(new_order)
        else:
            return {"error": "The product or the user dont exist"}, 400


class OrderResource(Resource):
    def get(self, order_id):
        order = Order.query.get_or_404(order_id)
        return order_schema.dump(order)



api.add_resource(OrderListResource, '/orders')
api.add_resource(OrderResource, '/orders/<int:order_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')