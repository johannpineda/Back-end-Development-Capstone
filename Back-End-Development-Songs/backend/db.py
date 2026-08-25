import os
from pymongo import MongoClient

def collection():
    uri=os.getenv('MONGO_URL','mongodb://localhost:27017')
    client=MongoClient(uri, serverSelectionTimeoutMS=1500)
    return client[os.getenv('MONGO_DB','band')][os.getenv('MONGO_COLLECTION','songs')]
