# Handles connection settings and client setup
from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER_URL = "localhost:9092"

def get_kafka_producer():
    return KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)

def get_kafka_consumer(topic):
    return KafkaConsumer(topic, bootstrap_servers=KAFKA_BROKER_URL)