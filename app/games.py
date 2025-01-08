from fastapi import APIRouter
from .schemas.games import ActiveGamesResponceSchema, ActiveGamesSchema, GameInfoResponceSchema, StatusSchema, GameOperationRequestSchema, HeroRequestSchema
from typing import List
from datetime import datetime

router = APIRouter()

@router.get("/active_games")
async def get_active_games() -> ActiveGamesResponceSchema:
    ""
    data: List[ActiveGamesSchema] = [
        ActiveGamesSchema(id=1, name="nm1", started_at=datetime(2011,1,1), price_rebuy=10, chip_count=1000, level_minutes=15, break_minutes=15),
        ActiveGamesSchema(id=2, name="nm2", started_at=datetime(2012,1,1), price_rebuy=20, chip_count=2000, level_minutes=25, break_minutes=25),
        ActiveGamesSchema(id=3, name="nm3", started_at=datetime(2013,1,1), price_rebuy=30, chip_count=3000, level_minutes=35, break_minutes=35),
        ActiveGamesSchema(id=4, name="nm4", started_at=datetime(2014,1,1), price_rebuy=40, chip_count=4000, level_minutes=45, break_minutes=45),
        ActiveGamesSchema(id=5, name="nm5", started_at=datetime(2015,1,1), price_rebuy=50, chip_count=5000, level_minutes=55, break_minutes=55),
        ]
    return ActiveGamesResponceSchema(status="ok", code=200, data=data)


@router.get("/game_info/{device_id}")
async def get_game_info(device_id: int) -> GameInfoResponceSchema:
    return GameInfoResponceSchema()

@router.post("/game_operation")
async def set_game_operation(request_data: GameOperationRequestSchema) -> StatusSchema:
    return StatusSchema(status="ok", code=request_data.operation)

@router.post("/rebuy_hero") #Если игра запущена, то игрок сразу становится "started_at=current_date"
async def set_rebuy_hero(request_data: HeroRequestSchema) -> StatusSchema:
    return StatusSchema(status="ok", code=200)

@router.post("/hero_end_game")
async def set_hero_end_game(request_data: HeroRequestSchema) -> StatusSchema:
    return StatusSchema(status="ok", code=200)
