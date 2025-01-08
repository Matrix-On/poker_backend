from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.game.tournaments import router as tournaments_router
from app import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tournaments_router, prefix='/game', tags=['tournaments'])
app.include_router(router)
