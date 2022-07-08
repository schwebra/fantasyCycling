from pymongo import MongoClient


class MongoDB:
    client = MongoClient("localhost", 27017)
    db = client.Cyclistdatabase

    def __init__(self) -> None:
        pass
