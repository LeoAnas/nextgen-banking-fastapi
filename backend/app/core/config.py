from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".envs/.env.local", env_ignore_empty=True,extra="ignore")
    PROJECT_NAME: str=""
    PROJECT_DESCRIPTION: str=""
    API_V1_STR: str=""
    SITE_NAME: str=""
    ENVIRONMENT: Literal["local", "staging", "production"]="local"
    DEBUG:bool=False


settings=Settings()
if not settings.DEBUG:
    print(settings.model_dump_json(indent=2))
