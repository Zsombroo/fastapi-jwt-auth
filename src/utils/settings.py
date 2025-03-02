from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    env: str

    jwt_secret_key: str
    jwt_alg: str
    jwt_access_token_exp_minutes: int
    jwt_refresh_token_exp_minutes: int
    jwt_issuer: str


    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str


settings = Settings()
