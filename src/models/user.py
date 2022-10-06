from datetime import date
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field


class Gender(str, Enum):
    m = 'Masculine'
    f = 'Feminine'


class BaseUser(BaseModel):
    email: str = Field(
        ...,
        description='User email'
    )
    username: str = Field(
        ...,
        description='Name used to identify users'
    )
    name: str = Field(
        ...,
        description='Full name'
    )
    birthday: date = Field(
        ...,
        description=''
    )
    gender: Gender = Field(
        ...,
        description=''
    )

    def dict(self, *, include: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None,
             exclude: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None, by_alias: bool = False,
             skip_defaults: Optional[bool] = None, exclude_unset: bool = False, exclude_defaults: bool = False,
             exclude_none: bool = False) -> 'DictStrAny':
        model_dict = super().dict(include=include, exclude=exclude, by_alias=by_alias, skip_defaults=skip_defaults,
                                  exclude_unset=exclude_unset, exclude_defaults=exclude_defaults,
                                  exclude_none=exclude_none)
        model_dict['birthday'] = str(self.birthday)
        return model_dict


class NewUserRequest(BaseUser):
    password: str = Field(
        ...,
        description=''
    )
    confirm_password: str = Field(
        ...,
        description=''
    )


class UserWithProducts(BaseUser):
    products: list = Field(
        ...,
        description=''
    )
