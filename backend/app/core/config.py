from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn,computed_field
from typing import Literal

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".envs/.env.local", env_ignore_empty=True,extra="ignore")
    PROJECT_NAME: str=""
    PROJECT_DESCRIPTION: str=""
    API_V1_STR: str=""
    SITE_NAME: str=""
    ENVIRONMENT: Literal["local", "staging", "production"]="local"
    DEBUG:bool=False
    # Postgres Settings
    POSTGRES_USER_NAME:str=""
    POSTGRES_PASSWORD:str=""
    POSTGRES_HOST:str=""
    POSTGRES_PORT:int=int("")
    @computed_field
    @property
    def POSTGRES_URL(self)->PostgresDsn:
       return PostgresDsn.build(scheme="postgresql+asyncpg",host=self.POSTGRES_HOST,port=self.POSTGRES_PORT,username=self.POSTGRES_USER_NAME,password=self.POSTGRES_PASSWORD,path="nextgen")


settings=Settings()
if not settings.DEBUG:
    print(settings.model_dump_json(indent=2))
