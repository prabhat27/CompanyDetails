from pymongo import MongoClient
import traceback

class DB:
    def __init__(self, db_port = 27017, db = 'test', db_host = 'localhost', db_collection = 'company_details3'):
        self.HOST = db_host
        self.COLLECTION = db_collection
        self.PORT = db_port
        self.DATABASE = db

    def insert_details(self, data):
        try:
            client = MongoClient(self.HOST, self.PORT)
            db = client[self.DATABASE]
            db[self.COLLECTION].remove({'website':data['website']})
            db[self.COLLECTION].insert(data)
        except:
            traceback.print_exc()
            return False
        return True