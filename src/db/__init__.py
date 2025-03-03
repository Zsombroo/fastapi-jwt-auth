from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


from src.utils.settings import settings


engine = create_engine(
    f"postgresql+psycopg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}",
    pool_size=10,
    # echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    with SessionLocal() as session:
        yield session


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attributes = [
            f"{key}={value!r}" for key, value in self.__dict__.items() if not key.startswith('_')
        ]
        return f"{class_name}({', '.join(attributes)})"


def init_db():
    Base.metadata.create_all(bind=engine)


def destroy_db():
    Base.metadata.drop_all(bind=engine)
