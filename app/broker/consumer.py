# Subscribes to Kafka or RabbitMQ topics
import json
from .config import get_kafka_consumer

def listen_to_topic(topic: str, handler_function):
    consumer = get_kafka_consumer(topic)
    for message in consumer:
        data = json.loads(message.value.decode("utf-8"))
        handler_function(data)
