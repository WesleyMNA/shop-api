import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient
from starlette import status

from src.db import get_mongo_connection
from src.main import app

client = TestClient(app)


def get_mongo_test_connection():
    _client = MongoClient('mongodb://localhost')
    db = _client['test_shop']

    try:
        yield db
    finally:
        _client.close()


app.dependency_overrides[get_mongo_connection] = get_mongo_test_connection


@pytest.fixture(autouse=True)
def tear_down():
    yield
    _client = MongoClient('mongodb://localhost')
    db = next(get_mongo_test_connection())
    _client.drop_database(db)


def test_register_user():
    data = {
        'email': 'user@email.com',
        'username': 'user',
        'name': 'User',
        'birthday': '2000-01-01',
        'gender': 'Masculine',
        'password': 'stringst',
        'confirm_password': 'stringst'
    }
    response = client.post('/api/v1/users', json=data)
    assert response.status_code == status.HTTP_201_CREATED
