from typing import Optional
from pydantic import BaseModel


class Player(BaseModel):
    username: str
    name: str


class UserCreate(BaseModel):
    username: str
    password: str
    name: str


class ShowUser(BaseModel):
    username: str
    name: str
    is_active: bool

    class Config():
        orm_mode = True

