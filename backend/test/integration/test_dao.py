import pytest
import unittest.mock as mock
from pymongo import errors
from bson.objectid import ObjectId

from src.util.dao import DAO

@pytest.mark.integration
def test_rule1_noncompliant():
    dao = DAO("user")
    obj = {'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}

    with pytest.raises(Exception) as e:
        created_obj1 = dao.create(obj)

        # delete if object was created in database
        id = created_obj1['_id']['$oid']
        dao.collection.delete_one({'_id': ObjectId(id)})
    assert e.type == errors.WriteError

@pytest.mark.integration
def test_rule2_noncompliant():
    dao = DAO("user")
    #functions shouldn't allow integers
    obj = {'firstName': 10, 'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}

    with pytest.raises(Exception) as e:
        created_obj1 = dao.create(obj)
        # delete if object was created in database
        id = created_obj1['_id']['$oid']
        dao.collection.delete_one({'_id': ObjectId(id)})
    assert e.type == errors.WriteError

@pytest.mark.integration
def test_3_noncompliant():
    """Should raise WriteError when creating multiple objects with the same email beacuse email has uniqueItems: true"""

    # Create objects
    dao = DAO("user")
    obj1 = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}
    obj2 = {'firstName': 'Enaj', 'lastName': 'Eod', 'email': 'jane.doe@gmail.com'}
    created_obj1 = dao.create(obj1)

    # Get id from object so we can delete it later
    objId1 = created_obj1['_id']['$oid']

    # Should raise exception when creating obj2 because the email is already in use
    with pytest.raises(Exception) as e:
            created_obj2 = dao.create(obj2)
            objId2 = created_obj2['_id']['$oid']
            # Delete both objects if no exception was raised earlier
            dao.collection.delete_one({'_id': ObjectId(objId2)})
            dao.collection.delete_one({'_id': ObjectId(objId1)})

    # Delete obj1 if an exception was raised because obj2 would never be created
    dao.collection.delete_one({'_id': ObjectId(objId1)})
    # Make sure the exception is a WriteError
    assert e.type == errors.WriteError


@pytest.mark.integration
def test_create():
    # Create objects
    dao = DAO("user")
    obj1 = {'firstName': 'Jane', 'lastName': 'Doe', 'email': 'jane.doe@gmail.com'}

    created_obj1 = dao.create(obj1)

    # Get id from object so we can delete it later
    objId1 = created_obj1['_id']['$oid']

    # Delete obj1 if an exception was raised because obj2 would never be created
    dao.collection.delete_one({'_id': ObjectId(objId1)})

    # remove id from created obj
    del created_obj1['_id']

    assert created_obj1 == obj1