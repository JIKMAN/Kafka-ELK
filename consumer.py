from kafka import KafkaConsumer
from json import loads
import time

if __name__ == "__main__":
    while:
        consumer = KafkaConsumer(
            'registered_user',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='latest',
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            consumer_timeout_ms=1000)
        
        for msg in consumer:
            print(f"Registered user ={msg.value}")     