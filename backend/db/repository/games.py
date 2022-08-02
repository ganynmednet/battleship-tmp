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
        num_rounds=settings.num_rounds,
        # current_round_id=current_round_id[0],
        ended=False,
        game_winner=None

    )

    # game.current_round = current_round

    db.add(game)
    db.commit()
    db.refresh(game)

    game_response = retrieve_round(game.id, db)
    # print("GAME RESPONSE")
    # print(game_response[0].__dict__)

    return game_response


def create_round(game_id: str, next_turn: str, db: Session):
    round_id = str(uuid.uuid4())
    new_round = Round(
        id=round_id,
        game_id=game_id,
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
    """
    https://hackersandslackers.com/sqlalchemy-data-models/
    """
    # print(db.query(Game, Round).join(Round).filter(Game.id == id).where(Round.game_id == Game.id).all())

    print(db.query(Game).join(Round, Round.game_id == Game.id).filter(Game.id == id))
    # item = db.query(Game, Round).join(Round).filter(Game.id == id).where(Round.game_id == Game.id).first()

    # items = db.query(Game).join(Round, Round.game_id == Game.id).filter(Game.id == id).all()

    # items = db.query(Game).join(Round, Round.game_id == Game.id).filter(Game.id == id).all()

    round = db.query(Round).join(Game, Round.game_id == Game.id).filter(Game.id == id).first()

    # print(items)
    # for round in items:
    game = {
        "id": round.parent_game.id,
        "name_player1": round.parent_game.name_player1,
        "name_player2": round.parent_game.name_player2,
        "num_rounds": round.parent_game.num_rounds,
        "ended": round.parent_game.ended,
        "game_winner": round.parent_game.game_winner,
        "current_round": {
            "id": round.id,
            "game_id": round.parent_game.id,
            "grid_player1": round.grid_player1,
            "grid_player2": round.grid_player2,
            "next_turn": round.next_turn,
            "round_winner": round.round_winner,
            "ended": round.ended
        }
    }

    print(game)

    return game
