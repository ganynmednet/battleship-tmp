from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.game import Game, Shoot
from db.session import get_db
from db.repository.games import shoot

router = APIRouter()


@router.get("/{game_id}/{hor}/{ver}", response_model=Game)
def make_shoot(db: Session = Depends(get_db)):
    """
    identify user! -> decrypt token or return error
    make shot
    """

    game = shoot({
        "game_id": game_id,
        "vertical": ver
        "horizontal": hor,
    }, db=db)

    return game
