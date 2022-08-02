from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, ARRAY, TypeDecorator, types, JSON
# from sqlalchemy import JSON, String, TypeDecorator
from sqlalchemy.orm import relationship
from db.base_class import Base
import json


class Round(Base):
    __tablename__ = 'round'
    id = Column(String, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("game.id"))
    parent_game = relationship("Game")
    grid_player1 = Column(JSON, nullable=False)
    grid_player2 = Column(JSON, nullable=False)
    next_turn = Column(String, nullable=True)
    round_winner = Column(String, nullable=True)
    ended = Column(Boolean(), default=False)


