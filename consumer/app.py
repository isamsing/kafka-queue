from kafka import KafkaConsumer
from random import randint

consumer = KafkaConsumer(
    bootstrap_servers='kafka:9092',
    group_id=f'test-group-{randint(0, 10)}',
    api_version=(0, 11, 5)
)

consumer.subscribe(topics=('kafka'))

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

if __name__ == '__main__':
    pass
