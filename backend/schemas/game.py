from pydantic import BaseModel
from typing import Any
from typing import Optional
from schemas.users import Player


class Round(BaseModel):
    id: str
    game_id: str
    grid_player1: list
    grid_player2: list
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

