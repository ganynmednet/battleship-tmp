from pydantic import BaseModel
from typing import Any
from typing import Optional, List
from schemas.users import Player


class Shoot(BaseModel):
    game_id: str
    user_id: str
    vertical: int
    horizontal: int


class Grid(BaseModel):
    user_id: str
    grid: list


# class Grids(BaseModel):
#     player1: Grid
#     player2: Grid


class Round(BaseModel):
    id: str
    game_id: str
    grids: List[Grid]
    # grid_player1: list
    # grid_player2: list
    next_turn: str
    round_winner: Optional[str]
    ended: str


class Game(BaseModel):
    id: str
    player1: Player
    player2: Player
    # current_round_id: str # must be Round object
    current_round: Round
    num_rounds: int
    played_rounds: Optional[list]
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
    player1_id: str
    player2_id: str
    num_rounds: Optional[int]
    ships: Ships
