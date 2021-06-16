from base import app, api, ma, db, Order, order_schema, orders_schema, q, process_order, Resource, Flask, request, jsonify



class OrderListResource(Resource):
    def get(self):
        orders = Order.query.all()
        return orders_schema.dump(orders)


class OrderResource(Resource):
    def get(self, order_id):
        order = Order.query.get_or_404(order_id)
        return order_schema.dump(order)



api.add_resource(OrderListResource, '/api-queries/orders')
api.add_resource(OrderResource, '/api-queries/orders/<int:order_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')