# error => faile to do handshake with server
# resolve
'''
1. Update your insert_data_mongodb method to this:
2. Go to MongoDB Atlas.

Click on Network Access (under Security in the left sidebar).

Click Add IP Address.

Click Allow Access From Anywhere (this adds 0.0.0.0/0) just for testing.

Wait about 60 seconds for the status to change from "Pending" to "Active," then run your script again.
'''




import os
import sys
import json

import collections
if not hasattr(collections, 'MutableMapping'):
    import collections.abc
    collections.MutableMapping = collections.abc.MutableMapping
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Added tlsAllowInvalidCertificates=True
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL, 
                tlsCAFile=ca, 
                tlsAllowInvalidCertificates=True
            )
            
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="NetworkSecurityProject"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
        


