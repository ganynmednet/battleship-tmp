from db.models.users import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import status
from core.security import decode_access_token


def get_user(username: str, db: Session):

    user = db.query(User).filter(User.username == username).first()

    return user


def get_current_user_from_token(token: str, db: Session):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    username = decode_access_token(token)

    if not username:
        raise credentials_exception

    user = get_user(username=username, db=db)

    if not user:
        raise credentials_exception

    return user
