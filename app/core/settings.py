from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    ENV: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache()
def get_settings() -> Settings:
    env_file = Path(".env")
    if not env_file.exists():
        raise FileNotFoundError(
            f".env file not found. Please create it from .env.example:\n"
            f"  cp .env.example .env\n"
            f"Then update DATABASE_URL with your PostgreSQL connection details."
        )
    return Settings()

