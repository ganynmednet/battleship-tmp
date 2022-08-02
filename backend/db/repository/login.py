from sqlalchemy.orm import Session
from db.models.users import User


def get_user(username: str, db: Session):

    # print(db.query(User).filter(User.username == username))
    # print(username)
    user = db.query(User).filter(User.username == username).first()

    # print(user.id)
    # print(user.user_id)
    return user
