

from pymongo import MongoClient
from fantasyCycling.database import MongoDB
from model import Stage

class StageService():
    db=MongoDB()
    collection=db.db.stages
    def __init__(self) -> None:
        pass
    
    def create_stage(self, stage: Stage):
        self.collection.insert_one(stage.__dict__)
        
    def find_stage_by_id(self, id: str):
        return self.collection.find_one({"_id": id})
    
    def find_stage_by_name(self, name: str):
        return self.collection.find_one({"name": name})
    