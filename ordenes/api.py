import requests
from worker import app, api, ma, db, Order, order_schema, orders_schema, q, process_order, Resource, Flask, request, jsonify

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
            q.enqueue(process_order, new_order.id)
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