import pytest
import unittest.mock as mock

from src.util.dao import DAO
from src.controllers.usercontroller import UserController

def test_valid_email_exists():

    # create data access object as a mock
    mockedDao = mock.MagicMock()

    # create the objects to be tested
    obj1 = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}
    obj2 = {'firstName': 'Jane2', 'lastName': 'Doe2', 'email': 'jane.doe@gmail.com'}
    obj_list = [obj1, obj2]

    # set return value of dao.find to obj_list
    mockedDao.find.return_value = obj_list

    # create a UserController with the data access object
    sut = UserController(mockedDao)

    # Run the function to be tested with the same email as the object we added
    validation_result = sut.get_user_by_email("jane.doe@gmail.com")

    # The get_user_by_email("jane.doe@gmail.com") should return the first object from the obj_list
    assert validation_result == obj1

def test_valid_email_not_exists():
    # create data access object as a mock
    mockedDao = mock.MagicMock()

    # set return value of dao.find to []
    mockedDao.find.return_value = []

    # create a UserController with the data access object
    sut = UserController(mockedDao)

    # Run the function with a valid email
    validation_result = sut.get_user_by_email("jane.doe@gmail.com")

    # The get_user_by_email("jane.doe@gmail.com") should return None
    assert validation_result == None


def test_invalid_email():

    # create data access object as a mock
    mockedDao = mock.MagicMock()

    # create the objects to be tested
    obj1 = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe.com'}
    obj_list = [obj1]

    # set return value of dao.find to obj_list
    mockedDao.find.return_value = obj_list

    # create a UserController with the data access object
    sut = UserController(mockedDao)

    # Test if the function raises the correct error
    with pytest.raises(ValueError) as e:
        sut.get_user_by_email("jane.doe.com")
    assert e.type == ValueError
