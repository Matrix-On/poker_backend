from fastapi import APIRouter
from .routers import router as games_router

api_games_router = APIRouter(prefix='/game', tags=["games"])

api_games_router.include_router(games_router)
