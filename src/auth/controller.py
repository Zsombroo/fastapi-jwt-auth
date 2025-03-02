from fastapi import HTTPException 
from fastapi import status

from src.users.model import User
from src.users.repository import get_user
from src.utils.security import create_access_token
from src.utils.security import create_refresh_token
from src.utils.security import verify_password
from src.utils.security import verify_token


def authenticate_user(
    username: str,
    password: str,
) -> User | None:
    user = get_user(username=username)

    if user is None or not verify_password(password, user.hashed_pw):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
 
    return user


def login(
    data: dict[str, str],
) -> dict[str, str]:
    user = authenticate_user(data["username"], data["password"])

    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def refresh(
    old_refresh_token: str,
) -> dict[str, str]:
    username = verify_token(old_refresh_token)
    user = get_user(username=username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }