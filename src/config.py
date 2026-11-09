from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from functools import lru_cache

class SETTINGS(BaseSettings):
    # Application information
    APP_NAME:str
    APP_VERSION:str
     
    # DB 
    MONGO_URL:str
    MONGO_DB_NAME:str
    
    MAX_UPLOAD_SIZE_MG:int   
    # Reading .env file
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def  get_settings() -> SETTINGS:
    return SETTINGS()