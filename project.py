from services.kafka import kafka_consumer, kafka_producer
from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import pandas as pd
import time

def kafka_producer():
    producer = KafkaProducer(
        value_serializer = lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092'],
    )

    return producer

def kafka_consumer():
    consumer = KafkaConsumer(
        'test_clase_kafka',
        #auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
        )
    for m in consumer:
       print(m.value)

cols = ["feature1","feature2","feature3", "y_test" ]
my_dataframe = pd.DataFrame(
    columns=cols,
    data=[
        (1,1,1,1),
        (2,2,2,2),
        (3,3,3,3),
        (4,4,4,4)
    ]
)


if __name__ == "__main__":

    producer = kafka_producer()
    
    for row in my_dataframe.values:
        producer.send("test_clase_kafka", value=str(row))
        time.sleep(3)
        print("message sent")
    
