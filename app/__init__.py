from fastapi import APIRouter
from .game import api_games_router

router = APIRouter()

router.include_router(api_games_router)
