from pydantic import BaseModel


class User(BaseModel):
    username: str
    hashed_pw: str
    teams: list[str] = []


class ProfileResponse(BaseModel):
    profile: str