from typing import Optional
from pydantic import BaseModel


class Player(BaseModel):
    username: str
    name: str


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    password: str
    name: str


class ShowUser(BaseModel):  # new
    username: str
    name: str
    is_active: bool

    class Config():  # tells pydantic to convert even non dict obj to json
        orm_mode = True

