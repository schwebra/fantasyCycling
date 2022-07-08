from model import User

from fantasyCycling.database import MongoDB


class UserService:
    db = MongoDB()
    collection = db.db.users

    def __init__(self) -> None:
        pass

    def create_user(self, user: User):
        self.collection.insert_one(user.parse_data_to_db())

    def find_user_by_id(self, id: dict):
        object_dict = self.collection.find_one({"_id": id})
        user = User(object_dict["name"], object_dict['username'], object_dict['password'])
        user._id = object_dict["_id"]
        user.substitutions = object_dict['substitutions']
        user.team = object_dict['team']
        user.stage_points_list = object_dict['stage_points_list']
        return user

    def find_user_by_name(self, name: str):
        object_dict = self.collection.find_one({"name": name})
        user = User(object_dict["name"], object_dict['username'], object_dict['password'])
        user._id = object_dict["_id"]
        user.substitutions = object_dict['substitutions']
        user.team = object_dict['team']
        user.stage_points_list = object_dict['stage_points_list']
        return user

    def update_user(self, user: User, variable: str, change: str):
        self.collection.update_one({"_id": user._id}, {"$set": {variable: change}})

    def delete_user_by_id(self, id: dict):
        return self.collection.delete_one({"_id": id})

    def make_substitution(self, cyclist_id_out: int, cyclist_id_in: int, user_id: int):
        user = self.find_user_by_id(user_id)
        user.team = [cyclist_id_in if cyclist == cyclist_id_out else cyclist for cyclist in user.team]
        user.make_substitution()
        self.update_user(user, 'team', user.team)
        self.update_user(user, 'subsititution', user.substitutions)
        