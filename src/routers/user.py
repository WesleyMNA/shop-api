from typing import List

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import Response

from src.models.user import BaseUser, NewUserRequest
from src.services import UserService

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('',
            response_model=List[BaseUser])
def list_all_users(service: UserService = Depends()):
    return service.list_all_users()


@router.post('',
             status_code=status.HTTP_201_CREATED,
             response_model=BaseUser)
def register_user(request: NewUserRequest,
                  service: UserService = Depends()):
    return service.register_user(request)


@router.put('/{username}',
            status_code=status.HTTP_204_NO_CONTENT)
def update_user(username: str,
                request,
                service: UserService = Depends()):
    service.update_user(username, request)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
