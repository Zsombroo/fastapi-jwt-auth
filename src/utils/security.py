from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Annotated

import jwt
from fastapi import Cookie
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from src.users.model import UserModel
from src.users.repository import get_user
from src.utils.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_refresh_token(
    refresh_token: str = Cookie(None),
) -> str:
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token not found"
        )
    return refresh_token


def get_password_hash(
    password: str,
) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def verify_token(
    token: str,
) -> str:
    payload = jwt.decode(
        jwt=token,
        key=settings.jwt_secret_key,
        algorithms=settings.jwt_alg,
    )
    if payload.get("iss") != settings.jwt_issuer or payload.get("tkn") not in ["refresh_token", "access_token"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    if datetime.now() >= datetime.fromtimestamp(payload.get("exp")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return payload.get("sub")
        

def create_access_token(
    user: UserModel,
) -> str:
    iss = settings.jwt_issuer
    sub = user.username
    exp = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_access_token_exp_minutes)
    tkn = "access_token"
    tms = user.teams
    payload = {
        "iss": iss,
        "sub": sub,
        "exp": exp,
        "tkn": tkn,
        "tms": tms,
    }
    encoded_jwt = jwt.encode(
        payload=payload,
        key=settings.jwt_secret_key,
        algorithm=settings.jwt_alg
    )
    return encoded_jwt


def create_refresh_token(
    user: UserModel,
) -> str:
    iss = settings.jwt_issuer
    sub = user.username
    exp = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_refresh_token_exp_minutes)
    tkn = "refresh_token"
    payload = {
        "iss": iss,
        "sub": sub,
        "exp": exp,
        "tkn": tkn,
    }
    encoded_jwt = jwt.encode(
        payload=payload,
        key=settings.jwt_secret_key,
        algorithm=settings.jwt_alg
    )
    return encoded_jwt


def current_user(
    token: Annotated[UserModel, Depends(oauth2_scheme)],
):
    username = verify_token(token)
    user = get_user(username=username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    
    return user