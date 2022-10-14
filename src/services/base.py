from abc import ABC

from pymongo import MongoClient
from pymongo.database import Database


class BaseService(ABC):

    def __init__(self, connection: dict, main_collection_name: str):
        self.client: MongoClient = connection['client']
        self.db: Database = connection['db']
        self.main_collection = self.db[main_collection_name]
