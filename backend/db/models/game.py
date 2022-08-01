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
    id = Column(String, primary_key=True, index=True)
    board = Column(JSON, nullable=False)
    player1 = Column(String, nullable=False)
    player2 = Column(String, nullable=False)
    move_turn = Column(String, nullable=True)
    ended = Column(Boolean(), default=False)
    winner = Column(String, nullable=True)
