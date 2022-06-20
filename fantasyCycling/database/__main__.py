from multiprocessing import connection
from sqlite3 import connect
from pymongo import MongoClient

class MongoDB:
    client = MongoClient("localhost", 27017)
    db = client['test']
    
    def __init__(self) -> None:
        pass

    
    @staticmethod
    def insert(self, collection, data):
        self.db[collection].insert(data)
    
    @staticmethod
    def find(self, collection, query):
        return self.db[collection].find(query)

    @staticmethod
    def find_one(self, collection, query):
        return self.db[collection].find_one(query)




if __name__ == '__main__':
    db = MongoDB()
    data = {"test": "test"}
    db.insert(db, "test", data)
    