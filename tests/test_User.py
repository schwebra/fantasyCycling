import pytest
from fantasyCycling.model import User, User
from fantasyCycling.service.UserService import UserService
from fantasyCycling.service.CyclistService import CyclistService


def test_that_user_can_be_persisted():
    test_user_service = UserService()
    test_user = User("test_user", "test", "password")
    test_user_service.create_user(test_user)
    test_user_id = test_user_service.find_user_by_name("test_user")._id
    assert test_user_service.find_user_by_id(test_user_id).name == "test_user"


def test_that_user_can_be_updated_by_id():
    test_user_service = UserService()
    test_user = test_user_service.find_user_by_name("test_user")
    test_user_service.update_user(test_user, "name", "updated_test_user")
    assert (
        test_user_service.find_user_by_id(test_user._id).name == "updated_test_user"
    )


def test_that_user_can_be_deleted_by_id():
    test_user_service = UserService()
    test_user = test_user_service.find_user_by_name("updated_test_user")
    test_user_service.delete_user_by_id(test_user._id)
    try:
        test_user_service.find_user_by_name("updated_test_user")
        assert False
    except TypeError:
        assert True
        

def test_that_a_subsitution_can_be_made():
    test_user_service = UserService()
    test_user_service.make_substitution(1,9,1)
    user =  test_user_service.find_user_by_id(1)
    assert user.substitutions == 7
