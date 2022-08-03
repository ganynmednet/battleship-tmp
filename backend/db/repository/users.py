from sqlalchemy.orm import Session
from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher
import uuid


def create_new_user(user: UserCreate, db: Session):
    user = User(
        id=str(uuid.uuid4()),
        username=user.username,
        name=user.name,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
