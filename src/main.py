from fastapi import FastAPI
from src.routes import base_route

app = FastAPI()

# App  routes
app.include_router(base_route)