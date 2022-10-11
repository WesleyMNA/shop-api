from abc import ABC

from pymongo import MongoClient
from pymongo.database import Database


class BaseService(ABC):

    def __init__(self, client: MongoClient, main_collection_name: str):
        self.db: Database = client['db']
        self.main_collection = self.db[main_collection_name]
