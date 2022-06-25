from lib2to3.pytree import Base
import uuid
from typing import List
from pydantic import BaseModel


class Cyclist(BaseModel):
    _id = None
    stage_results = []

    def __init__(self, name: str, value: int, team: str) -> None:
        self.name = name
        self.value = value
        self.team = team

    def add_stage_result(stage_result):
        stage_result.append(stage_result)


class Stage():
    _id = None
    def __init__(self, name: str) -> None:
        self.name = name

    def parse_data_to_db(self):
        return {
            "name": self.name
        }


class StagePoints(BaseModel):
    def __init__(
        self,
        stage_rank: int,
        sprint_points: int,
        mountain_points: int,
        gc_rank: int,
        points_rank: int,
        mountains_rank: int,
        most_combative: bool,
        stage: str,
    ) -> None:
        self.id = uuid.uuid1()
        self.stage_rank = stage_rank
        self.sprint_points = sprint_points
        self.mountain_points = mountain_points
        self.gc_rank = gc_rank
        self.mountain_rank = mountains_rank
        self.points_rank = points_rank
        self.most_combative = most_combative
        self.stage = stage

    def stage_result_points(self) -> int:
        total = 0
        if self.stage_rank == 1:
            total += 200
        elif self.stage_rank == 2:
            total += 150
        elif self.stage_rank == 3:
            total += 120
        elif self.stage_rank == 4:
            total += 100
        elif self.stage_rank == 5:
            total += 90
        elif self.stage_rank == 6:
            total += 80
        elif self.stage_rank == 7:
            total += 70
        elif self.stage_rank == 8:
            total += 65
        elif self.stage_rank == 9:
            total += 60
        elif self.stage_rank == 10:
            total += 55
        elif self.stage_rank == 11:
            total += 50
        elif self.stage_rank == 12:
            total += 45
        elif self.stage_rank == 13:
            total += 40
        elif self.stage_rank == 14:
            total += 35
        elif self.stage_rank == 15:
            total += 30
        elif self.stage_rank == 16:
            total += 25
        elif self.stage_rank == 17:
            total += 20
        elif self.stage_rank == 18:
            total += 15
        elif self.stage_rank == 19:
            total += 10
        elif self.stage_rank == 20:
            total += 9
        elif self.stage_rank > 20:
            total += 8
        elif self.stage_rank > 25:
            total += 7
        elif self.stage_rank > 30:
            total += 6
        elif self.stage_rank > 35:
            total += 5
        elif self.stage_rank > 40:
            total += 4
        elif self.stage_rank > 50:
            total += 3
        elif self.stage_rank > 60:
            total += 2
        elif self.stage_rank > 80 and self.stage_rank < 101:
            total += 1

        total += self.mountain_points
        total += self.sprint_points
        if self.most_combative:
            total += 30
        return total

    def rankings_points(self) -> int:
        total = 0
        # generalClassification
        if self.gc_rank == 1:
            total += 50
        elif self.gc_rank == 2:
            total += 45
        elif self.gc_rank == 3:
            total += 40
        elif self.gc_rank == 4:
            total += 35
        elif self.gc_rank == 5:
            total += 30
        elif self.gc_rank == 6:
            total += 28
        elif self.gc_rank == 7:
            total += 26
        elif self.gc_rank == 8:
            total += 24
        elif self.gc_rank == 9:
            total += 22
        elif self.gc_rank == 10:
            total += 21
        elif self.gc_rank == 11:
            total += 20
        elif self.gc_rank == 12:
            total += 19
        elif self.gc_rank == 13:
            total += 18
        elif self.gc_rank == 14:
            total += 17
        elif self.gc_rank == 15:
            total += 16
        elif self.gc_rank == 16:
            total += 15
        elif self.gc_rank == 17:
            total += 14
        elif self.gc_rank == 18:
            total += 13
        elif self.gc_rank == 19:
            total += 12
        elif self.gc_rank == 20:
            total += 11
        elif self.gc_rank > 20:
            total += 10
        elif self.gc_rank > 25:
            total += 9
        elif self.gc_rank > 30:
            total += 8
        elif self.gc_rank > 35:
            total += 7
        elif self.gc_rank > 40:
            total += 5
        elif self.gc_rank > 50:
            total += 3
        elif self.gc_rank > 60:
            total += 2
        elif self.gc_rank > 80 and self.gc_rank < 101:
            total += 1

        # pointsclass
        if self.points_rank == 1:
            total += 30
        elif self.points_rank == 2:
            total += 26
        elif self.points_rank == 3:
            total += 22
        elif self.points_rank == 4:
            total += 20
        elif self.points_rank == 5:
            total += 18
        elif self.points_rank == 6:
            total += 16
        elif self.points_rank == 7:
            total += 14
        elif self.points_rank == 8:
            total += 12
        elif self.points_rank == 9:
            total += 10
        elif self.points_rank == 10:
            total += 8
        elif self.points_rank == 11:
            total += 6
        elif self.points_rank == 12:
            total += 4
        elif self.points_rank == 13:
            total += 3
        elif self.points_rank == 14:
            total += 2
        elif self.points_rank == 15:
            total += 1

        # mountains
        if self.mountains_rank == 1:
            total += 30
        elif self.mountains_rank == 2:
            total += 26
        elif self.mountains_rank == 3:
            total += 22
        elif self.mountains_rank == 4:
            total += 20
        elif self.mountains_rank == 5:
            total += 18
        elif self.mountains_rank == 6:
            total += 16
        elif self.mountains_rank == 7:
            total += 14
        elif self.mountains_rank == 8:
            total += 12
        elif self.mountains_rank == 9:
            total += 10
        elif self.mountains_rank == 10:
            total += 8
        elif self.mountains_rank == 11:
            total += 6
        elif self.mountains_rank == 12:
            total += 4
        elif self.mountains_rank == 13:
            total += 3
        elif self.mountains_rank == 14:
            total += 2
        elif self.mountains_rank == 15:
            total += 1
        return total

    def stage_total_points(self):
        return self.rankings_points(self) + self.stage_result_points(self)


class User(BaseModel):
    id: str = None
    team: List[str] = []
    stage_points_list: List[str] = []
    data_dict = {
    }
    
    def __init__(self, name: str, username: str, password: str) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.substitutions = 8
    
    def __init__(self, data_dict: dict) -> None:
        pass

    def make_substitution(self) -> None:
        self.substitutions -= 1
