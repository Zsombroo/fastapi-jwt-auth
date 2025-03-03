from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.db import init_db
from src.db import destroy_db
from src.auth.api import router as auth_router
from src.users.api import router as user_router


@asynccontextmanager
async def lifespan():
    # Initialize
    init_db()

    # Run
    yield

    # Clean up
    destroy_db()


app = FastAPI(
    lifespan=lifespan,
)


app.include_router(auth_router)
app.include_router(user_router)
