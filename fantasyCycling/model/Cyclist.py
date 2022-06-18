import uuid


class Cyclist:
    stage_results = []

    def __init__(self, name, value) -> None:
        self.id = uuid.uuid1()
        self.name = name
        self.value = value

    def add_stage_result(stage_result):
        stage_result.append(stage_result)
