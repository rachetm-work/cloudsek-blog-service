import json
import logging

import pika

from src.framework.es.es_manager import ESManager
from src.framework.settings.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def callback(ch, method, properties, body):
    try:
        entry = json.loads(body)
        index_name_suffix = entry.pop("index_name_suffix", '')
        ESManager(index_name_suffix=index_name_suffix).index_single(record=entry)
        logger.info(f"Indexed blog entry with id: {entry['id']}")
    except Exception as e:
        logger.error(f"Error indexing blog entry: {str(e)}")


def consume_queue():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.rabbitmq_host, port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='blog_queue')
        channel.basic_consume(queue='blog_queue', on_message_callback=callback, auto_ack=True)
        logger.info("Consumer started. Waiting for messages...")
        channel.start_consuming()
    except Exception as e:
        logger.error(f"Error in consumer: {str(e)}")


if __name__ == "__main__":
    consume_queue()
