from pydantic import BaseSettings


class DBSettings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_SCHEMA: str
    DB_HOST: str
    DB_PORT: int

    class Config:
        env_file = ".env"
