from fastapi import APIRouter,Depends
from src.config import get_settings, SETTINGS

base_route = APIRouter(
    prefix="/api/v0.1.0",
    tags=["Base-settings"]
)

@base_route.get("/app-info")
def get_info(app_info:SETTINGS=Depends(get_settings)):
    return{
        "app name": app_info.APP_NAME,
        "app version": app_info.APP_VERSION,
    }