from pydantic import BaseModel


class Move(BaseModel):
    row: str
    column: str


class MoveResult(BaseModel):
    hit: bool
