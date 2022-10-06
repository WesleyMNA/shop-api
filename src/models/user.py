from datetime import date
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, validator, EmailStr

from src.core import encrypt_password
from src.db import user_collection


class Gender(str, Enum):
    m = 'Masculine'
    f = 'Feminine'


class BaseUser(BaseModel):
    email: EmailStr = Field(
        ...,
        description='User email',
        example='user@email.com'
    )
    username: str = Field(
        ...,
        description='Name used to identify users',
        example='user'
    )
    name: str = Field(
        ...,
        description="User's full name",
        example='User'
    )
    birthday: date = Field(
        ...,
        description="User's birthday",
        example='2000-01-01'
    )
    gender: Gender = Field(
        ...,
        description="User's gender"
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

    @validator('email')
    def validate_email(cls, value):
        user = user_collection.find_one({'email': value})

        if user is not None:
            raise ValueError('Email already used')
        return value

    @validator('username')
    def validate_username(cls, value):
        user = user_collection.find_one({'username': value})

        if user is not None:
            raise ValueError('Username already used')
        return value

    @validator('confirm_password')
    def passwords_match(cls, value, values):
        if 'password' in values and value != values['password']:
            raise ValueError('Passwords do not match')
        values['password'] = encrypt_password(value)
        return value

    def dict(self, *, include: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None,
             exclude: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None, by_alias: bool = False,
             skip_defaults: Optional[bool] = None, exclude_unset: bool = False, exclude_defaults: bool = False,
             exclude_none: bool = False) -> 'DictStrAny':
        model_dict = super().dict(include=include, exclude=exclude, by_alias=by_alias, skip_defaults=skip_defaults,
                                  exclude_unset=exclude_unset, exclude_defaults=exclude_defaults,
                                  exclude_none=exclude_none)
        del model_dict['confirm_password']
        return model_dict


class UserWithProducts(BaseUser):
    products: list = Field(
        ...,
        description=''
    )
