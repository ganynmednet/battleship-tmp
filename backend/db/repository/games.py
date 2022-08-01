import uuid
import random
from sqlalchemy.orm import Session
from schemas.game import GameCreate
from db.models.game import Game


def create_new_game(settings: GameCreate, db: Session):
    # print(settings)
    game = Game(
        id=str(uuid.uuid4()),
        board=[[0] * settings.board_size for _ in range(settings.board_size)],
        player1=settings.player1,
        player2=settings.player2,
        move_turn=random.choice([settings.player1, settings.player2]),
        ended=False,
        winner=None
    )
    # print(type(game.board))
    db.add(game)
    db.commit()
    db.refresh(game)

    # item = db.query(Game).filter(Game.id == game.id).first()
    # print(item.player1)
    return game


def retrieve_game(id: str, db: Session):
    item = db.query(Game).filter(Game.id == id).first()
    return item
