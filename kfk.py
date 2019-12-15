import kafka

kafka_client = kafka.KafkaClient('localhost:9092')

producer = kafka.SimpleProducer(kafka_client)

producer.send_messages('my-topic', 'message1')
producer.send_messages('my-topic', 'message2')
producer.send_messages('my-topic', 'message3')

consumer = kafka.KafkaConsumer(
    'my-topic', group_id='my_group',
    bootstrap_servers=['localhost:9092'])

for message in consumer:
    print("topic: %s message=%s" % (message.topic, message.value))

