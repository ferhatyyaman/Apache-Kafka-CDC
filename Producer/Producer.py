from kafka import KafkaProducer
from pymongo import MongoClient
import json
import time
import schedule

# MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['CDC_database']
collection = db['CDC_collection']

# Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Function to fetch new documents and send them to Kafka
def job():
    docs = collection.find({"new": True})
    for doc in docs:
        producer.send('your_topic', doc)
        collection.update_one({"_id": doc["_id"]}, {"$set": {"new": False}})

# Schedule job every 10 seconds
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
