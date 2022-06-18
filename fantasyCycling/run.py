from model.Cyclist import Cyclist
from model.Stage import Stage
from model.StagePoints import StagePoints
from model.User import User


def main():
    cyclist1 = Cyclist("Chis Froome", 30)
    print(cyclist1.id)

if __name__ == "__main__":
    main()