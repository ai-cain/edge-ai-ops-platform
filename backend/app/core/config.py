from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Edge AI Ops Platform API"
    api_prefix: str = "/api/v1"
    database_url: str = Field(
        default="postgresql+psycopg://edgeops:edgeops@localhost:5432/edge_ai_ops"
    )
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
