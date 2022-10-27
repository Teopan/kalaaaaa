from pymongo import *

class Database:
    def __init__(self):
        # Provide the mongodb atlas url to connect python to mongodb using pymong
        #url
        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        self.client = MongoClient(self.CONNECTION_STRING)
    
    # Create the database for our example (we will use the same database throughout the tutorial
    def get_database(self):
        return self.client['quotes']
    
    
    def runner(self, name, data):
        dbname = self.get_database()
        collection_name = dbname[name]
        collection_name.insert_one(data)
    
    def get_collection(self, name):
        dbname = self.get_database()
        collection_name = dbname[name]
        item_details = collection_name.find()

        return item_details
