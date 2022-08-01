from pydantic import BaseModel
from typing import Any
from typing import Optional

# class Board(BaseModel):
#     data: list


class Game(BaseModel):
    id: str
    board: list
    player1: str
    player2: str
    move_turn: str
    ended: bool
    winner: Optional[str]

    class Config():  # tells pydantic to convert even non dict obj to json
        orm_mode = True


class Ships(BaseModel):
    battleship: bool
    carrier: bool
    destroyer: bool


class GameCreate(BaseModel):
    player1: str
    player2: str
    board_size: int
    num_turns: int
    ships: Ships
    # num_ships
    # max_ship_size = 5
    # min_ship_size = 2
