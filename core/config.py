from __future__ import annotations
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.engine.url import URL

DIR = Path(__file__).absolute().parent.parent
CORE_DIR = Path(__file__).absolute().parent

class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8',extra="ignore")



class DBSettings(EnvBaseSettings):
    DB_HOST: str = 'db'
    DB_PORT: int = 5433
    DB_USER: str = 'postgres'
    DB_PASS: str | None = '12345'
    DB_NAME: str = 'poker_db'

    @property
    def database_url(self) -> URL | str:
        if self.DB_PASS:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def database_url_psycopg2(self) -> str:
        if self.DB_PASS:
            return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

class AlembicSettings(EnvBaseSettings):
    DATABASE_URL_ALEMBIC: str | None = None
    ALEMBIC_CONFIG_PATH: str = str(Path(__file__).parent.parent / 'alembic.ini')

    @property
    def database_url_alembic(self) -> str:
        if not self.DATABASE_URL_ALEMBIC:
            raise ValueError("Alembic database URL is not set")
        return self.DATABASE_URL_ALEMBIC


class Settings(DBSettings, AlembicSettings):
    DEBUG: bool = False
    AUTH_SECRET_KEY: str


settings = Settings()
