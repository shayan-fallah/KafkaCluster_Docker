from kafka import KafkaProducer
import jason
import socket
import time


def json_serializer(obje):
    return json.dumps(obje).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['kafka-one:9092', 'kafka-two:9093', 'kafka-three:9094'],
    value_serializer=json_serializer
)
if __name__ == "__main__":
    while 1 == 1:
        hostname = socket.gethostname()
        host_ip_address = socket.gethostbyname(hostname)
        data = {hostname: host_ip_address}
        print(data)
        producer.send("topicname", data)
        time.sleep(5)
