import pytest

from fantasyCycling.model import Cyclist, User
from fantasyCycling.service.CyclistService import CyclistService


def test_that_cyclist_can_be_persisted():
    test_cyclist_service = CyclistService()
    test_cyclist = Cyclist("test_cyclist", 20, "Ineos")
    test_cyclist_service.create_cyclist(test_cyclist)
    test_cyclist_id = test_cyclist_service.find_cyclist_by_name("test_cyclist")._id
    assert test_cyclist_service.find_cyclist_by_id(test_cyclist_id).name == "test_cyclist"


def test_that_cyclist_can_be_updated_by_id():
    test_cyclist_service = CyclistService()
    test_cyclist = test_cyclist_service.find_cyclist_by_name("test_cyclist")
    test_cyclist_service.update_cyclist(test_cyclist, "name", "updated_test_cyclist")
    assert (
        test_cyclist_service.find_cyclist_by_id(test_cyclist._id).name == "updated_test_cyclist"
    )


def test_that_cyclist_can_be_deleted_by_id():
    test_cyclist_service = CyclistService()
    test_cyclist = test_cyclist_service.find_cyclist_by_name("updated_test_cyclist")
    test_cyclist_service.delete_cyclist_by_id(test_cyclist._id)
    try:
        test_cyclist_service.find_cyclist_by_name("updated_test_cyclist")
        assert False
    except TypeError:
        assert True
