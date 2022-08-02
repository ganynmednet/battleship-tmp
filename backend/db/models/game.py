from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, ARRAY, TypeDecorator, types, JSON
# from sqlalchemy import JSON, String, TypeDecorator
from sqlalchemy.orm import relationship
from db.base_class import Base
import json


class Json(TypeDecorator):

    @property
    def python_type(self):
        return object

    impl = types.String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_literal_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        try:
            return json.loads(value)
        except (ValueError, TypeError):
            return None


class Game(Base):
    """
    https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    """
    __tablename__ = 'game'
    id = Column(String, primary_key=True, index=True)
    # grid_player1 = Column(JSON, nullable=False)
    # grid_player2 = Column(JSON, nullable=False)
    name_player1 = Column(String, nullable=False)
    name_player2 = Column(String, nullable=False)
    # move_turn = Column(String, nullable=True)
    current_round_id = Column(String, ForeignKey("round.id"), nullable=False)
    current_round = relationship("Round")
    ended = Column(Boolean(), default=False)
    game_winner = Column(String, nullable=True)
    __mapper_args__ = {
        "polymorphic_identity": "game"
    }
