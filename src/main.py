from fastapi import FastAPI

from src.auth.api import router as auth_router
from src.users.api import router as user_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
