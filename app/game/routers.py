from fastapi import APIRouter, Depends
from typing import Annotated
from app.game.handlers import GameHandler
from ..schemas.games import ActiveGamesResponceSchema, ActiveGamesSchema,\
        GameInfoResponceSchema, StatusSchema, GameOperationRequestSchema,\
        HeroRequestSchema, NewGameRequestSchema, NewGameResponceSchema

router = APIRouter()

@router.get("/active_games", responses={200:{"model" : ActiveGamesResponceSchema}})
async def get_active_games(handler: Annotated[GameHandler, Depends(GameHandler)]) -> ActiveGamesResponceSchema:
    return await handler.get_active_games()

@router.get("/game_info/{game_id}", responses={200:{"model" : GameInfoResponceSchema}})
async def get_game_info(game_id: int,
                        handler: Annotated[GameHandler, Depends(GameHandler)]) -> GameInfoResponceSchema:
    return await handler.get_game_info(game_id)

@router.post("/game_operation")
async def set_game_operation(request_data: GameOperationRequestSchema) -> StatusSchema:
    return StatusSchema(status="ok", code=request_data.operation)

@router.post("/rebuy_hero") #Если игра запущена, то игрок сразу становится "started_at=current_date"
async def set_rebuy_hero(request_data: HeroRequestSchema) -> StatusSchema:
    return StatusSchema(status="ok", code=200)

@router.post("/hero_end_game")
async def set_hero_end_game(request_data: HeroRequestSchema) -> StatusSchema:
    return StatusSchema(status="ok", code=200)

@router.post("/new_game")
async def set_new_game(request_data: NewGameRequestSchema) -> NewGameResponceSchema:
    return NewGameResponceSchema(status="ok", code=200, game_id=request_data.tournament_id)
