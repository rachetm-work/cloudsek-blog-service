import json

import pika

from src.framework.settings.settings import settings


def publish_to_queue(message: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.rabbitmq_host))
    channel = connection.channel()
    channel.queue_declare(queue='blog_queue')
    channel.basic_publish(exchange='', routing_key='blog_queue', body=json.dumps(message))
    connection.close()
