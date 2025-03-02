from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.controller import login
from src.auth.controller import refresh
from src.auth.model import TokenResponse
from src.utils.security import get_refresh_token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def api_login(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> TokenResponse:
    tokens = login(
        data={
            "username": form_data.username,
            "password": form_data.password,
        },
    )
    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
    )
    return {"access_token": tokens["access_token"]}


@router.post(path='/refresh', response_model=TokenResponse)
async def api_refresh(
    response: Response,
    refresh_token: str = Depends(get_refresh_token),
) -> TokenResponse:
    tokens = refresh(
        old_refresh_token=refresh_token,
    )
    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
    )
    return {"access_token": tokens["access_token"]}