from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

# 1. Ensure no < > brackets around the password
# 2. Add 'certifi' to handle SSL on Windows
uri = "mongodb+srv://mcs2025005_db_user:<@password>@ac-ek573t4-shard-00-00.ikd2zed.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
