import json
from .config import get_kafka_producer

producer = get_kafka_producer()

def publish_event(topic: str, data: dict):
    producer.send(topic, json.dumps(data).encode("utf-8"))
    producer.flush()
