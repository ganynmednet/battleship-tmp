import uuid
import random
from sqlalchemy.orm import Session
from schemas.game import GameCreate
from db.models.game import Game
from db.models.round import Round


def create_new_game(settings: GameCreate, db: Session):
    game_id = str(uuid.uuid4())

    current_round_id = create_round(
        game_id=game_id,
        next_turn=random.choice([settings.name_player1, settings.name_player2]),
        db=db
    ),
    # print(dir(current_round))
    # print(type(current_round))
    # # print(current_round.__getitem__("id"))
    # print(current_round.__dict__)

    game = Game(
        id=game_id,
        name_player1=settings.name_player1,
        name_player2=settings.name_player2,
        current_round_id=current_round_id[0],
        ended=False,
        game_winner=None

    )

    # game.current_round = current_round

    db.add(game)
    db.commit()
    db.refresh(game)

    return game


def create_round(game_id: str, next_turn: str, db: Session):

    round_id = str(uuid.uuid4())
    new_round = Round(
        id=round_id,
        # game_id=game_id,
        grid_player1=[[0] * 10 for _ in range(10)],
        grid_player2=[[0] * 10 for _ in range(10)],
        next_turn=next_turn,
        ended=False,
        round_winner=None
    )
    db.add(new_round)
    db.commit()
    db.refresh(new_round)

    return round_id


def retrieve_game(id: str, db: Session):
    item = db.query(Game).filter(Game.id == id).first()
    # item = db.query(Game)

    return item


def retrieve_round(id: str, db: Session):

    print(db.query(Game, Round).join(Round).filter(Game.id == id).where(Round.id == Game.current_round_id))

    item = db.query(Game, Round).join(Round).filter(Game.id == id).where(Round.id == Game.current_round_id).first()

    # item = db.query(Game).join(Round).where(Round.id == Game.id).first()
    print(item)
    return item