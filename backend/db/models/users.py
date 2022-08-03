from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    def __repr__(self):
        return f"<User {self.id}>"