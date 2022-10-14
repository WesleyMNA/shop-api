from pymongo import MongoClient


def get_mongo_connection():
    client = MongoClient('mongodb://localhost')
    db = client['shop']

    try:
        yield db
    finally:
        client.close()
