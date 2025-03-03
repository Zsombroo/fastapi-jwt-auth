import pytest

from src.db import destroy_db
from src.db import init_db
from src.db import get_session
from src.db.schemas import User
from src.utils.security import get_password_hash


def populate_db():
    with next(get_session()) as session:
        session.add(User(
            username="testuser",
            email="hello@there.com",
            hashed_password=get_password_hash("testpassword"),
        ))
        session.commit()
        

@pytest.fixture(autouse=True)
def manage_db():
    init_db()
    populate_db()
    yield
    destroy_db()
