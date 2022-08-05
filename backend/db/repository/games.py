import uuid
import random
from sqlalchemy.orm import Session
from sqlalchemy import or_
from schemas.game import GameCreate, Shoot
from db.models.game import Game
from db.models.round import Round
from db.models.users import User
from core.game_functions.board_generator import generate_board
from core.game_functions.shoot import perform_shoot


def shoot(shoot: Shoot, db: Session):
    """
    get game
    get oponents board
    make shoot
    save board
    respond
    """
    print(shoot)
    _round = retrieve_round(shoot["game_id"], db)

    board: list

    for player in _round["grids"]:
        if player["user_id"] == shoot["user_id"]:
            board = player["grid"]

    shoot_ = (shoot["vertical"], shoot["horizontal"])

    # opponent's board
    board = perform_shoot(board, shoot_)

    for player in _round["grids"]:
        if player["user_id"] == shoot["user_id"]:
            player["grid"] = board

    # print(board)

    print("NEW GRID")
    print(_round["grids"])
    update_data = {
        "data": _round["grids"]
    }
    print("NEW GRID")
    # https://docs.sqlalchemy.org/en/14/tutorial/data_update.html
    print(db.query(Round).filter(Round.id == shoot["game_id"]).update({Round.grids: update_data}, synchronize_session=False))
    db.query(Round).filter(Round.id == shoot["game_id"]).update({Round.grids: update_data}, synchronize_session=False)

    game = retrieve_game(shoot["game_id"], db)

    return game


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
        player1_id=settings.player1_id,
        player2_id=settings.player2_id,
        ships=dict(settings.ships),
        next_turn=random.choice([settings.player1_id, settings.player2_id]),
        db=db
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    game_response = retrieve_game(game.id, db)

    return game_response


def retrieve_round(game_id, db) -> Game:
    _round = retrieve_game(game_id, db)
    return _round["current_round"]


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


def create_round(game_id: str, ships: dict, next_turn: str, player1_id:str, player2_id:str, db: Session):
    round_id = str(uuid.uuid4())
    new_round = Round(
        id=round_id,
        game_id=game_id,
        grid_player1=generate_board(ships),
        grid_player2=generate_board(ships),
        grids={
            "data": [
                {
                    "user_id": player1_id,
                    "grid": generate_board(ships)
                },
                {
                    "user_id": player2_id,
                    "grid": generate_board(ships)
                }
            ]
        },
        next_turn=next_turn,
        ended=False,
        round_winner=None
    )
    db.add(new_round)
    db.commit()
    db.refresh(new_round)

    return round_id


def retrieve_game(game_id: str, db: Session):
    """
    https://hackersandslackers.com/sqlalchemy-data-models/
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm
    """

    # print(db.query(Round, Game).outerjoin(Game, Round.game_id == Game.id).filter(Game.id == game_id))

    round = db.query(Round).join(Game, Round.game_id == Game.id).filter(Game.id == game_id).first()

    # print([g for g in round.grids["data"]])
    # grids = []
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
            # "grids": [
            #     {
            #         "user_id": round.parent_game.player1.id,
            #         "grid": round.grid_player1
            #     },
            #     {
            #         "user_id": round.parent_game.player2.id,
            #         "grid": round.grid_player2
            #     }
            # ],
            "grids": round.grids["data"],
            "next_turn": round.next_turn,
            "round_winner": round.round_winner,
            "ended": round.ended
        }
    }

    # print(game)

    return game
