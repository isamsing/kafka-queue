from kafka import KafkaConsumer
from random import randint

consumer = KafkaConsumer(
    ('kafka'),
    security_protocol="SSL",
    bootstrap_servers='kafka:9092',
    group_id=f'test-group-{randint(0, 10)}',
    api_version=(0, 11, 5)
)


for message in consumer:
    print(message)

if __name__ == '__main__':
    pass
