from abc import ABC

from pymongo import MongoClient
from pymongo.database import Database


class BaseService(ABC):

    def __init__(self, db: Database, main_collection_name: str):
        if main_collection_name not in db.list_collection_names():
            db.create_collection(main_collection_name)

        self.db: Database = db
        self.main_collection = self.db[main_collection_name]
