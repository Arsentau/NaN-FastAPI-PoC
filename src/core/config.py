from functools import lru_cache
from typing import List, Optional

from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    version: Optional[str] = "Default Mode"
    debug: Optional[bool] = True
    host: Optional[str] = "0.0.0.0"
    port: Optional[int] = 8000
    allow_origins: Optional[List[str]] = ["*"]
    allow_credentials: Optional[List[str]] = ["*"]
    allow_methods: Optional[List[str]] = ["*"]
    allow_headers: Optional[List[str]] = ["*"]
    title: Optional[str] = "FastApi Poc"

    class Config:
        env_file = ".env"


class DbSettings(BaseSettings):
    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_name: str
    pgadmin_default_email: str
    pgadmin_default_password: str

    class Config:
        env_file = ".env.database"


class DbMigrationsSettings(BaseSettings):
    postgres_host: str = "localhost"
    postgres_port: int = "5432"
    postgres_user: str = "fastapi"
    postgres_password: str = "fastapi"
    postgres_name: str = "fastapi"
    pgadmin_default_email: str = "fastapi@db.com"
    pgadmin_default_password: str = "fastapi"

    class Config:
        env_file = "../.env.database"


class Settings:

    @lru_cache
    def get_api_settings() -> ApiSettings:
        return ApiSettings()

    @lru_cache
    def get_db_settings() -> DbSettings:
        try:
            return DbSettings()
        except Exception:
            return DbMigrationsSettings()

    @lru_cache
    def get_db_alembic_settings() -> DbMigrationsSettings:
        return DbMigrationsSettings()
