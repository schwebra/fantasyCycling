from model import StagePoints

from fantasyCycling.database import MongoDB


class StagePointsService:
    db = MongoDB()
    collection = db.db.stagePoints

    def __init__(self) -> None:
        pass

    def create_stagePoints(self, stagePoints: StagePoints):
        self.collection.insert_one(stagePoints.parse_data_to_db())

    def find_stagePoints_by_id(self, id: dict):
        object_dict = self.collection.find_one({"_id": id})
        stagePoints = StagePoints(object_dict["name"], object_dict['stage_id'], object_dict['stage_rank'], object_dict['sprint_points'], object_dict['mountain_points'], object_dict['gc_rank'], object_dict['points_rank'], object_dict['mountains_rank'], object_dict['most_combative'])
        stagePoints._id = object_dict["_id"]
        return stagePoints

    def find_stagePoints_by_name(self, name: str):
        object_dict = self.collection.find_one({"name": name})
        stagePoints = StagePoints(object_dict["name"], object_dict['stage_id'], object_dict['stage_rank'], object_dict['sprint_points'], object_dict['mountain_points'], object_dict['gc_rank'], object_dict['points_rank'], object_dict['mountains_rank'], object_dict['most_combative'])
        stagePoints._id = object_dict["_id"]
        return stagePoints

    def update_stagePoints(self, stagePoints: StagePoints, variable: str, change: str):
        self.collection.update_one({"_id": stagePoints._id}, {"$set": {variable: change}})

    def delete_stagePoints_by_id(self, id: dict):
        return self.collection.delete_one({"_id": id})
