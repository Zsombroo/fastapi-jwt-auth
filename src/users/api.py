from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from src.users.model import User
from src.utils.security import current_user
from src.utils.logging import logger


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/profile")
def api_profile(
    user: Annotated[User, Depends(current_user)]
):
    logger.debug(user)
    return "Success"
