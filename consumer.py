from kafka import KafkaConsumer

consumer = KafkaConsumer('aaa', bootstrap_servers='localhost:32769')
for msg in consumer:
    print(msg)
