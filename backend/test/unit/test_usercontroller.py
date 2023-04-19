import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

@pytest.mark.unit
@pytest.mark.parametrize("objList, expected", [
    #one match
    ([{'firstName': 'Jane',  'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}],
      # expected value
      {'firstName': 'Jane',  'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}),
    #Two matches
    ([{'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@gmail.com'},
      {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}],
      # expected value
      {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}),
    #no matches
    ([], None)
])
def test_emails(objList, expected):
    # Create a mock that returns the parametrized values
    mockedDao = mock.MagicMock()
    mockedDao.find.return_value = objList

    # Create sut with the mock
    sut = UserController(mockedDao)

    # Check if correct value is returned
    validationResult = sut.get_user_by_email("jane.doe@gmail.com")
    assert validationResult == expected

@pytest.mark.unit
def test_invalid_email():
    # create a mock of database
    mockedDao = mock.MagicMock()

    # Define what the mock should respond with
    obj1 = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe.com'}
    obj_list = [obj1]
    mockedDao.find.return_value = obj_list

    # create sut with the mock
    sut = UserController(mockedDao)

    # Check if a valueError is raised when mail is incorrect.
    with pytest.raises(ValueError) as e:
        sut.get_user_by_email("jane.doe.com")
    assert e.type == ValueError