import pytest
from fantasyCycling.model import StagePoints, User, Stage
from fantasyCycling.service.StagePointsService import StagePointsService


def test_that_stagePoints_can_be_persisted():
    test_stagePoints_service = StagePointsService()
    test_stagePoints = StagePoints("test_stage_points", "1", 10, 10, 10, 10, 10, 10, True)
    test_stagePoints_service.create_stagePoints(test_stagePoints)
    test_stagePoints_id = test_stagePoints_service.find_stagePoints_by_name("test_stage_points")._id
    assert test_stagePoints_service.find_stagePoints_by_id(test_stagePoints_id).name == "test_stage_points"


def test_that_stagePoints_can_be_updated_by_id():
    test_stagePoints_service = StagePointsService()
    test_stagePoints = test_stagePoints_service.find_stagePoints_by_name("test_stage_points")
    test_stagePoints_service.update_stagePoints(test_stagePoints, "name", "updated_test_stagePoints")
    assert (
        test_stagePoints_service.find_stagePoints_by_id(test_stagePoints._id).name == "updated_test_stagePoints"
    )


def test_that_stagePoints_can_be_deleted_by_id():
    test_stagePoints_service = StagePointsService()
    test_stagePoints = test_stagePoints_service.find_stagePoints_by_name("updated_test_stagePoints")
    test_stagePoints_service.delete_stagePoints_by_id(test_stagePoints._id)
    try:
        test_stagePoints_service.find_stagePoints_by_name("updated_test_stagePoints")
        assert False
    except TypeError:
        assert True