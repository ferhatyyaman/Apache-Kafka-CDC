
from pymongo.mongo_client import MongoClient
import pymongo

uri = "mongodb://ferhatyaman:12345@ac-3jbaqke-shard-00-00.9io1zj3.mongodb.net:27017,ac-3jbaqke-shard-00-01.9io1zj3.mongodb.net:27017,ac-3jbaqke-shard-00-02.9io1zj3.mongodb.net:27017/?ssl=true&replicaSet=atlas-11x3w9-shard-0&authSource=admin&retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

    