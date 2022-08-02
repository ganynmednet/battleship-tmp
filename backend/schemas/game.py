from pydantic import BaseModel
from typing import Any
from typing import Optional


class Round(BaseModel):
    id: str
    game_id: str
    grid_player1: list
    grid_player2: list
    next_turn: str
    round_winner: str
    ended: str


class Game(BaseModel):
    id: str
    name_player1: str
    name_player2: str
    current_round: str # must be Round object
    ended: bool
    game_winner: Optional[str]

    class Config():  # tells pydantic to convert even non dict obj to json
        orm_mode = True


class Ships(BaseModel):
    carrier: Optional[bool]  # 5
    battleship: Optional[bool]  # 4
    cruiser: Optional[bool]  # 3
    destroyer: Optional[bool]  # 2


class GameCreate(BaseModel):
    name_player1: str
    name_player2: str
    # board_size: int
    num_rounds: Optional[int]
    ships: Ships
    # num_ships
    # max_ship_size = 5
    # min_ship_size = 2
