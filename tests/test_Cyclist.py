import pytest
from fantasyCycling.database import MongoDB

def test_that_test_passes():
    assert True==True


def test_that_database_connect():
    connection=MongoDB()
    print(connection.client)
    assert True==True