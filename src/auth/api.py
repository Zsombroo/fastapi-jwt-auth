from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.controller import login
from src.auth.controller import refresh
from src.utils.security import get_refresh_token


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def api_login(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> JSONResponse:
    tokens = login(
        data={
            "username": form_data.username,
            "password": form_data.password,
        },
    )

    response = JSONResponse(
        content={"access_token": tokens["access_token"]},
    )
    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
    )
    return response


@router.post(path='/refresh')
async def api_refresh(
    response: Response,
    refresh_token: str = Depends(get_refresh_token),
) -> JSONResponse:
    tokens = refresh(
        old_refresh_token=refresh_token,
    )

    response = JSONResponse(
        content={"access_token": tokens["access_token"]},
    )
    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=True,
        samesite="lax",
    )
    return response