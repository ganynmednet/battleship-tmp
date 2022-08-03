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
    https://hackersandslackers.com/sqlalchemy-data-models/
    """
    __tablename__ = 'game'
    id = Column(String, primary_key=True, index=True)
    player1_id = Column(String, ForeignKey("user.id"))
    player2_id = Column(String, ForeignKey("user.id"))
    num_rounds = Column(Integer, nullable=False)
    ended = Column(Boolean(), default=False)
    game_winner = Column(String, nullable=True)

    player1 = relationship("User", foreign_keys=[player1_id])
    player2 = relationship("User", foreign_keys=[player2_id])

    def __repr__(self):
        return f"<Game {self.id}>"
