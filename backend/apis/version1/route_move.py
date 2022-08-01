from fastapi import APIRouter
from schemas.move import Move, MoveResult

router = APIRouter()


@router.post("/", response_model=MoveResult)
def move(move: Move):
    # get
    result = None
    return result
