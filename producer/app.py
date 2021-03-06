import json
from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(
    bootstrap_servers=['kafka:19092'],
    api_version=(0, 11, 5),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

count = 0
while True:
    print(f"Seding {count} ...")
    producer.send('kafka', count)
    count += 1
    print(f"... Done")
    sleep(5)

if __name__ == '__main__':
    pass
