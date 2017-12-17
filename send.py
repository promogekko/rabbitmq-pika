#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('51.255.211.244'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
