from kafka import KafkaProducer


brokers=["localhost:9092"]
topic="s3rashu"

producer=KafkaProducer(bootstrap_servers=brokers)

def messageSender(message):
    producer.send(topic,message.encode('utf-8'))