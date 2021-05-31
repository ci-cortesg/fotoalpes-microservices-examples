from api import db, Order
import pika
import time
import requests

time.sleep(30)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    message = body.decode()
    order_id = int(message)
    order = Order.query.get(order_id)
    product = requests.get(f"http://products:5000/products/{order.product}")
    product = product.json()
    if product['stock'] >= order.quantity:
        requests.put(f"http://products:5000/products/{order.product}", json={'stock': product['stock']-order.quantity})
        order.state = "completed"
    else:
        order.state = "failed"
    db.session.commit()
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()