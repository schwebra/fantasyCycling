from typing_extensions import assert_type
import pytest
from fantasyCycling.model import Stage, User
from fantasyCycling.service.StageService import StageService


def test_that_stage_can_be_persisted():
    test_stage_service = StageService()
    test_stage = Stage("test_stage")
    test_stage_service.create_stage(test_stage)
    test_stage_id= test_stage_service.find_stage_by_name("test_stage")._id
    assert test_stage_service.find_stage_by_id(test_stage_id).name == 'test_stage'

def test_that_stage_can_be_updated_by_id():
    test_stage_service = StageService()
    test_stage = test_stage_service.find_stage_by_name("test_stage")
    test_stage_service.update_stage(test_stage, 'name', "updated_test_stage")
    assert test_stage_service.find_stage_by_id(test_stage._id).name == 'updated_test_stage'
    
    
def test_that_stage_can_be_deleted_by_id():
    test_stage_service = StageService()
    test_stage = test_stage_service.find_stage_by_name("updated_test_stage")
    test_stage_service.delete_stage_by_id(test_stage._id)
    try:
        test_stage_service.find_stage_by_name("updated_test_stage")
        assert False
    except TypeError:
        assert True