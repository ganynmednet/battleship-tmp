from pydantic import BaseModel
from typing import List


# class Board(BaseModel):
#     data: list


class Board(BaseModel):
    board: list
