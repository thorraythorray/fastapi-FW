from enum import IntEnum
from tortoise import fields

from app.core.base.model import BaseOrmModel


class Role(BaseOrmModel):
    name = fields.CharField(max_length=32)


class GenderEnum(IntEnum):
    UNKOWN = 0
    MALE = 1
    FEMALE = 2


class User(BaseOrmModel):
    name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=128)
    phone = fields.CharField(max_length=16, null=True)
    age = fields.IntField(null=True)
    sex = fields.IntEnumField(enum_type=GenderEnum, default=0)
    avatar = fields.CharField(max_length=255, null=True)
    is_active = fields.BooleanField(default=True)
    role = fields.ForeignKeyField(Role, related_name='users', on_delete=fields.SET_NULL, null=True)