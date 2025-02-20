from fastapi import APIRouter, Depends
from typing import Annotated
from app.game.handlers import GameHandler
from ..schemas.games import ActiveGamesResponceSchema, TournamentsResponceSchema,\
        GameInfoResponceSchema, StatusSchema, GameOperationRequestSchema,\
        HeroRequestSchema, NewGameRequestSchema, NewGameResponceSchema,\
        HeroesResponceSchema, HeroesInGameResponceSchema

router = APIRouter()

@router.get("/tournaments", responses={200: {"model" : TournamentsResponceSchema}})
async def get_tournaments(handler: Annotated[GameHandler, Depends(GameHandler)]) -> TournamentsResponceSchema:
    return await handler.get_tournaments()

@router.get("/heroes", responses={200: {"model" : HeroesResponceSchema}})
async def get_heroes(handler: Annotated[GameHandler, Depends(GameHandler)]) -> HeroesResponceSchema:
    return await handler.get_heroes()

@router.get("/active_games", responses={200:{"model" : ActiveGamesResponceSchema}})
async def get_active_games(handler: Annotated[GameHandler, Depends(GameHandler)]) -> ActiveGamesResponceSchema:
    return await handler.get_active_games()

@router.get("/game_info/{game_id}", responses={200:{"model" : GameInfoResponceSchema}})
async def get_game_info(game_id: int,
                        handler: Annotated[GameHandler, Depends(GameHandler)]) -> GameInfoResponceSchema:
    return await handler.get_game_info(game_id)

@router.get("/hero_in_game/{game_id}", responses={200:{"model" : HeroesInGameResponceSchema}})
async def get_hero_in_game(game_id: int,
                        handler: Annotated[GameHandler, Depends(GameHandler)]) -> HeroesInGameResponceSchema:
    return await handler.get_hero_in_game(game_id)

@router.post("/game_operation", responses={200:{"model" : NewGameResponceSchema}})
async def set_game_operation(request_data: GameOperationRequestSchema,
                             handler: Annotated[GameHandler, Depends(GameHandler)]) -> StatusSchema:
    return  await handler.set_game_operation(request_data)

@router.post("/rebuy_hero", responses={200:{"model" : NewGameResponceSchema}})
async def set_rebuy_hero(request_data: HeroRequestSchema,
                         handler: Annotated[GameHandler, Depends(GameHandler)]) -> StatusSchema:
    return await handler.set_rebuy_hero(request_data)

@router.post("/new_game", responses={200:{"model" : NewGameResponceSchema}})
async def set_new_game(request_data: NewGameRequestSchema,
                       handler: Annotated[GameHandler, Depends(GameHandler)]) -> NewGameResponceSchema:
    return await handler.set_new_game(request_data)
