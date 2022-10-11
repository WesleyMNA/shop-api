from typing import List

from fastapi import Depends
from pymongo import MongoClient

from src.models.user import BaseUser, NewUserRequest
from .base import BaseService
from ..db import get_mongo_client


class UserService(BaseService):

    def __init__(self, client: MongoClient = Depends(get_mongo_client), main_collection_name: str = 'user'):
        super().__init__(client, main_collection_name)

    def list_all_users(self) -> List[BaseUser]:
        users = self.main_collection.find({}, {'products': 0})
        return [BaseUser(**user) for user in users]

    def register_user(self, request: NewUserRequest) -> BaseUser:
        result = self.main_collection.insert_one(request.dict())
        user = self.main_collection.find_one({'_id': result.inserted_id})
        return BaseUser(**user)
