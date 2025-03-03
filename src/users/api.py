from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from src.users.model import ProfileResponse
from src.users.model import UserModel
from src.utils.security import current_user
from src.utils.logging import logger


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/profile", response_model=ProfileResponse)
def api_profile(
    user: Annotated[UserModel, Depends(current_user)],
) -> ProfileResponse:
    logger.debug(user)
    return {"profile": "Success"}
