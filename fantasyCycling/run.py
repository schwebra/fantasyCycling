from model import Cyclist, Stage, StagePoints, User
from database import MongoDB

def main():
    cyclist1 = Cyclist("Chis Froome", 30)
    print(cyclist1.__dict__)
    db = MongoDB()
    collection = db.db.cyclists
    collection.insert_one(cyclist1.__dict__)


if __name__ == "__main__":
    main()
