from src.db import get_session
from src.db.schemas import User
from src.users.model import UserModel


def get_user(
    username: str,
) -> UserModel | None:
    with next(get_session()) as session:
        user = session.query(User).filter(User.username == username).one_or_none()
    
    if user:
        user = UserModel(
            id=user.id,
            username=user.username,
            hashed_password=user.hashed_password,
        )
    
    return user
