import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings defines the configurational settings"""

    app_env: str
    app_host: str
    app_port: str
    base_url: str
    redis_host: str
    redis_port: str
    redis_db: str

    model_config = SettingsConfigDict(env_file=os.getenv("ENV_FILE", ".env"))


@lru_cache
def get_settings() -> Settings:
    return Settings()
