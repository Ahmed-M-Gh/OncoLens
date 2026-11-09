from pymongo import MongoClient
from pymongo.database import Database
from src.config import get_settings
settings = get_settings()
from src.schemas.enums import ResponseEnum

if not settings.MONGO_URL :
    raise ValueError(ResponseEnum.MognoDBURLNotFound)
if not settings.MONGO_DB_NAME :
    raise ValueError(ResponseEnum.MognoDBNameNotFound)

# Create Client
client = MongoClient(
    settings.MONGO_URL,
    serverSelectionTimeoutMS=5000
)

db: Database = client[settings.MONGO_DB_NAME]

def check_connection():
    client.admin.command("ping")
    
    return True

def close_connection():
    client.close()
    