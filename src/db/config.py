from pymongo import MongoClient


def get_mongo_connection():
    client = MongoClient('mongodb://localhost')
    db = client['shop']

    try:
        yield {
            'client': client,
            'db': db
        }
    finally:
        client.close()
