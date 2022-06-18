from model.Cyclist import Cyclist
from model.StagePoints import StagePoints
from typing import List
import uuid


class User:
    team: List[Cyclist]=[]
    stage_points_list: List[StagePoints]=[]
    def __init__(self, name: str, username: str, password: str) -> None:
        self.id = uuid.uuid1()
        self.name=name
        self.username=username
        self.password=password
        self.substitutions=8
        
    def make_substitution(self) -> None:
        self.substitutions-=1