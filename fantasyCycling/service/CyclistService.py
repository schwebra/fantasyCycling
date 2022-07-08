from model import Cyclist

from fantasyCycling.database import MongoDB


class CyclistService:
    db = MongoDB()
    collection = db.db.cyclists

    def __init__(self) -> None:
        pass

    def create_cyclist(self, cyclist: Cyclist):
        self.collection.insert_one(cyclist.parse_data_to_db())

    def find_cyclist_by_id(self, id: dict):
        object_dict = self.collection.find_one({"_id": id})
        cyclist = Cyclist(object_dict["name"], object_dict['value'], object_dict['team'])
        cyclist._id = object_dict["_id"]
        return cyclist

    def find_cyclist_by_name(self, name: str):
        object_dict = self.collection.find_one({"name": name})
        cyclist = Cyclist(object_dict["name"], object_dict['value'], object_dict['team'])
        cyclist._id = object_dict["_id"]
        cyclist.stage_results = object_dict['stage_results']
        return cyclist

    def update_cyclist(self, cyclist: Cyclist, variable: str, change: str):
        self.collection.update_one({"_id": cyclist._id}, {"$set": {variable: change}})

    def delete_cyclist_by_id(self, id: dict):
        return self.collection.delete_one({"_id": id})
