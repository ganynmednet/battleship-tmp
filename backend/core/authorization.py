from functools import wraps
from fastapi import status, HTTPException, Depends
from core.security import decode_access_token
from db.repository.login import get_user


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # db: Session = Depends(get_db)

        headers = {key.decode(): val.decode() for key, val in dict(kwargs["request"]["headers"]).items()}
        user = decode_access_token(headers['authorization'].split()[1])

        user = get_user(username=user["sub"], db=kwargs["db"])
        kwargs["user"] = user

        return func(*args, **kwargs)

    return wrapper