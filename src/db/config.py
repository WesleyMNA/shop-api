from pymongo import MongoClient


def get_mongo_client():
    cluster = MongoClient('mongodb://localhost/shop')

    try:
        yield cluster
    finally:
        cluster.close()
