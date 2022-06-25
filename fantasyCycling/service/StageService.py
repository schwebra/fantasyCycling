

from pymongo import MongoClient
from fantasyCycling.database import MongoDB
from model import Stage
from pydantic import parse_obj_as
import logging

class StageService():
    db=MongoDB()
    collection=db.db.stages
    def __init__(self) -> None:
        pass
    
    def create_stage(self, stage: Stage):
        self.collection.insert_one(stage.parse_data_to_db())
        
    def find_stage_by_id(self, id: dict):
        object_dict = self.collection.find_one({"_id": id})
        try:
            stage = Stage(object_dict['name'])
            stage._id = object_dict['_id']
        except TypeError:
            return logging.error("No object found")
        return stage
    
    def find_stage_by_name(self, name: str):
        object_dict = self.collection.find_one({"name": name})
        stage = Stage(object_dict['name'])
        stage._id = object_dict['_id']
        return stage
    
    def update_stage(self, stage: Stage, variable: str, change: str):
        self.collection.update_one({'_id': stage._id}, { "$set":{variable:change}})
    
    def delete_stage_by_id(self, id: dict):
        return self.collection.delete_one({"_id": id})
    