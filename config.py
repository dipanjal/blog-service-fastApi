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


class JWTSettings(BaseSettings):
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
