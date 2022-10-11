from typing import List

from fastapi import Depends
from pymongo import MongoClient

from src.models.user import BaseUser, NewUserRequest
from .base import BaseService
from ..db import get_mongo_client
from ..models import Conflict


class UserService(BaseService):

    def __init__(self,
                 client: MongoClient = Depends(get_mongo_client)):
        super().__init__(client, 'user')

    def list_all_users(self) -> List[BaseUser]:
        users = self.main_collection.find({}, {'products': 0})
        return [BaseUser(**user) for user in users]

    def register_user(self, request: NewUserRequest) -> BaseUser:
        if self.main_collection.find_one({'email': request.email}) is not None:
            raise Conflict('Email already used')

        if self.main_collection.find_one({'username': request.username}) is not None:
            raise Conflict('Username already used')

        result = self.main_collection.insert_one(request.dict())
        user = self.main_collection.find_one({'_id': result.inserted_id})
        return BaseUser(**user)
