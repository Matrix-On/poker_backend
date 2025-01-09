from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from database.requests import active_games, get_game_info,\
    get_game_operations, get_game_heroes, create_new_game
from app.schemas.games import ActiveGamesResponceSchema, ActiveGamesSchema,\
        GameInfoResponceSchema, StatusSchema, GameOperationRequestSchema,\
        HeroRequestSchema, NewGameRequestSchema, NewGameResponceSchema,\
        HeroesSchema, OperationsSchema

class GameHandler:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    def Error(self, message: str, code: int = 400):
        raise HTTPException(status_code=code, detail=message)



    async def get_active_games(self) -> ActiveGamesResponceSchema:
        try:
            result = await active_games(self.session)
            data = [ActiveGamesSchema(**game) for game in result]
            return ActiveGamesResponceSchema(data=data)
        except HTTPException as e:
            return self.Error(message=str(e))

    async def get_game_info(self, game_id: int) -> GameInfoResponceSchema:
        try:
            game_info = await get_game_info(self.session, game_id)
            if (not game_info):
                return self.Error(message='Invalid request parameters')
            game_heroes = await get_game_heroes(self.session, game_id)
            game_operations = await get_game_operations(self.session, game_id)

            game_heroes = [HeroesSchema(**gh.__dict__) for gh in game_heroes]
            game_operations = [OperationsSchema(**go.__dict__) for go in game_operations]
            game_info = ActiveGamesSchema(**game_info)

            return GameInfoResponceSchema(game=game_info, heroes=game_heroes, operations=game_operations)
        except HTTPException as e:
            return self.Error(message=str(e))

    async def set_game_operation(self, request_data: GameOperationRequestSchema) -> StatusSchema:
        try:
            return ""
        except HTTPException as e:
            return self.Error(message=str(e))

    async def set_rebuy_hero(self, request_data: HeroRequestSchema) -> StatusSchema:
        try:
            return ""
        except HTTPException as e:
            return self.Error(message=str(e))

    async def set_hero_end_game(self, request_data: HeroRequestSchema) -> StatusSchema:
        try:
            return ""
        except HTTPException as e:
            return self.Error(message=str(e))

    async def set_new_game(self, request_data: NewGameRequestSchema) -> NewGameResponceSchema:
        try:
            if (request_data.tournament_id < 1):
                return self.Error(message='Invalid request parameters')
            game_id = await create_new_game(self.session, request_data.tournament_id)
            return NewGameResponceSchema(game_id=game_id)
        except HTTPException as e:
            return self.Error(message=str(e))
