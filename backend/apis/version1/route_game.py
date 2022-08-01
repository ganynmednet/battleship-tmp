from fastapi import APIRouter, Depends, HTTPException, status
from schemas.game import Game
from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.games import retrieve_game

router = APIRouter()


@router.get("/{id}", response_model=Game)
def get_game(id: str, db: Session = Depends(get_db)):

    game = retrieve_game(id=id, db=db)

    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Game with this id {id} does not exist")

    return game
