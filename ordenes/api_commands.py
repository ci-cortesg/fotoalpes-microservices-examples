from base import app, api, ma, db, Order, User, Product, order_schema, orders_schema, q, process_order, Resource, Flask, request, jsonify



class OrderListResource(Resource):

    def post(self):
        user = User.query.get(request.json['user'])
        product = Product.query.get(request.json['product'])
        if user is not None and product is not None:
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




api.add_resource(OrderListResource, '/api-commands/orders')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')