from typing import List

from src.db import user_collection
from src.models.user import BaseUser, NewUserRequest


def list_all_users() -> List[BaseUser]:
    users = user_collection.find({}, {'products': 0})
    return [BaseUser(**user) for user in users]


def register_user(request: NewUserRequest) -> BaseUser:
    result = user_collection.insert_one(request.dict())
    user = user_collection.find_one({'_id': result.inserted_id})
    return BaseUser(**user)
