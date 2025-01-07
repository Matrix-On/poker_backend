from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.tournaments import router as tournaments_router
from app.games import router as games_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tournaments_router, prefix='/game', tags=['tournaments'])
app.include_router(games_router, prefix='/game', tags=['games'])
