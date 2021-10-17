from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        'topicname',
        bootstrap_servers=['kafka-one:9092', 'kafka-two:9093', 'kafka-three:9094'],
        auto_offset_reset='earliest',
        group_id='one-consumer'
    )
    for message in consumer:
        print(json.loads(message.value.decode('utf-8')))