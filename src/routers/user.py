from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from src.models.user import BaseUser, NewUserRequest
from src.services import user

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('',
            response_model=List[BaseUser])
def list_all_users(all_users: List[BaseUser] = Depends(user.list_all_users)):
    return all_users


@router.post('',
             status_code=status.HTTP_201_CREATED,
             response_model=BaseUser)
def register_user(request: NewUserRequest):
    return user.register_user(request)
