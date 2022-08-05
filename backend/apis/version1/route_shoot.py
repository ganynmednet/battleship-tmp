from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import Union
from schemas.game import Game, Shoot
# from db.models.users import User
from db.session import get_db
from db.repository.games import shoot
from core.authorization import auth_required
from typing import Union, Any

router = APIRouter()


# @router.get("/{game_id}/{hor}/{ver}", response_model=Game)
# def make_shoot1(request: Request, game_id: str, ver: int, hor: int, db: Session = Depends(get_db)):
#     """
#     identify user! -> decrypt token or return error
#     make shot
#     """
#
#     game = shoot({
#         "game_id": game_id,
#         "vertical": ver,
#         "horizontal": hor,
#     }, db=db)
#
#     return game


@router.get("/{game_id}/{hor}/{ver}", response_model=Game)
@auth_required
def make_shoot(request: Request,
               game_id: str,
               ver: int,
               hor: int,
               db: Session = Depends(get_db),
               user: Union[Any, None] = None
               ):
    """
    identify user! -> decrypt token or return error
    make shot
    """

    payload = {
        "game_id": game_id,
        "user_id": user.id,
        "vertical": ver,
        "horizontal": hor,
    }
    print(payload)
    game = shoot(payload, db=db)

    return game
