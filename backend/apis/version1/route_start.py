from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.game import GameCreate, Game
from db.session import get_db
from db.repository.games import create_new_game

router = APIRouter()


@router.post("/", response_model=Game)
def create_game(settings: GameCreate, db: Session = Depends(get_db)):

    game = create_new_game(settings=settings, db=db)
    return game
