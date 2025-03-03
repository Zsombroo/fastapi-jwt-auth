from . import Base
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class UserTeamJunction(Base):
    __tablename__ = "user_team_junction"

    user_id = mapped_column(ForeignKey("user_account.id"), primary_key=True)
    team_id = mapped_column(ForeignKey("team.id"), primary_key=True)

    role: Mapped[str] = mapped_column(String(20))


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)

    teams: Mapped[list["Team"]] = relationship(
        "Team",
        secondary=UserTeamJunction.__table__,
        back_populates="users"
    )


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_name: Mapped[str] = mapped_column(String(30))

    users: Mapped[list["User"]] = relationship(
        "User",
        secondary=UserTeamJunction.__table__,
        back_populates="teams"
    )
