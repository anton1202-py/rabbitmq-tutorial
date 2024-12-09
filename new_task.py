import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
message = " ".join(sys.argv[1:]) or "Hello World!..............."

channel.basic_publish(
    exchange="logs",
    routing_key="",
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
    ),
    body=message,
)

print(f" [x] Sent {message}")
connection.close()
