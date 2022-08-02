from typing import Optional
from pydantic import BaseModel


class Player(BaseModel):
    name: str
    id: str


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    password: str


class ShowUser(BaseModel):  # new
    username: str
    is_active: bool

    class Config():  # tells pydantic to convert even non dict obj to json
        orm_mode = True
