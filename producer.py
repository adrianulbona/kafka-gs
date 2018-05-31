from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:32769')
for _ in range(100):
    producer.send('aaa', b'aaaa')
