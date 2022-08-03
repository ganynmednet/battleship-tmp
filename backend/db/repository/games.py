import uuid
import random
from sqlalchemy.orm import Session
from sqlalchemy import or_
from schemas.game import GameCreate
from db.models.game import Game
from db.models.round import Round
from db.models.users import User


def create_new_game(settings: GameCreate, db: Session):
    game_id = str(uuid.uuid4())

    game = Game(
        id=game_id,
        player1_id=settings.player1_id,
        player2_id=settings.player2_id,
        num_rounds=settings.num_rounds,
        ended=False,
        game_winner=None

    )

    create_round(
        game_id=game_id,
        next_turn=random.choice([settings.player1_id, settings.player2_id]),
        db=db
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    # get_game(game.id, db)

    game_response = retrieve_game(game.id, db)

    return game_response


# def get_game(game_id, db):
#     print("GAME ID")
#     res = db.query(Game).filter(Game.id == game_id).first()
#
#     print(
#         res.id,
#         res.player1_id,
#         res.player2_id
#     )
#     print("GAME ID")


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
    """
    https://hackersandslackers.com/sqlalchemy-data-models/
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm
    """

    print(db.query(Round, Game).outerjoin(Game, Round.game_id == Game.id).filter(Game.id == id))

    round = db.query(Round).join(Game, Round.game_id == Game.id).filter(Game.id == id).first()

    game = {
        "id": round.parent_game.id,
        "player1": {
            "username": round.parent_game.player1.username,
            "name": round.parent_game.player1.name
        },
        "player2": {
            "username": round.parent_game.player2.username,
            "name": round.parent_game.player2.name
        },
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

    # print(game)

    return game
