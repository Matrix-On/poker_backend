from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from core.timezone import timezone
from typing import List

from database.database import get_async_session
from database.requests import active_games, get_game_info,\
    get_game_operations, get_game_heroes, create_new_game, get_blinds_info,\
    add_game_hero, update_game_hero_state, game_is_start, update_game_start,\
    add_game_opertaion, update_game_end, move_game_to_history, get_tournaments,\
    get_heroes, get_heroes_in_game
from app.schemas.games import ActiveGamesResponceSchema, ActiveGamesSchema,\
        GameInfoResponceSchema, StatusSchema, GameOperationRequestSchema,\
        HeroRequestSchema, NewGameRequestSchema, NewGameResponceSchema,\
        HeroesSchema, OperationsSchema, GameInfoSchema, BlindsSchema,\
        TournamentsResponceSchema, GameInfoDataSchema, TournamentsSchema,\
        HeroesResponceSchema, HeroesGameSchema, HeroesInGameSchema,\
        HeroesInGameResponceSchema
from core.enums import HeroOpertaionsEnum, GameOperationsEnum

class GameHandler:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    def Error(self, message: str, code: int = 400):
        raise HTTPException(status_code=code, detail=message)

    def InvalidRequestParameters(self):
        self.Error(message='Invalid request parameters')


    async def get_tournaments(self) -> TournamentsResponceSchema:
        try:
            result = await get_tournaments(self.session)
            data = [TournamentsSchema(**tournament[0].__dict__) for tournament in result]
            return TournamentsResponceSchema(data=data)
        except HTTPException as e:
            return self.Error(message=str(e))

    async def get_heroes(self) -> HeroesResponceSchema:
        try:
            result = await get_heroes(self.session)
            data = [HeroesSchema(**hero[0].__dict__) for hero in result]
            return HeroesResponceSchema(data=data)
        except HTTPException as e:
            return self.Error(message=str(e))

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
                return self.InvalidRequestParameters()
            game_blinds = await get_blinds_info(self.session, game_id)
            game_heroes = await get_game_heroes(self.session, game_id)
            game_operations = await get_game_operations(self.session, game_id)

            game_heroes = [HeroesGameSchema(**gh[0].__dict__, fullname=gh[0].heroes.fullname) for gh in game_heroes]
            game_operations = [OperationsSchema(**go[0].__dict__) for go in game_operations]
            game_info = GameInfoSchema(**game_info, blinds=[BlindsSchema(**blinds) for blinds in game_blinds])

            return GameInfoResponceSchema(data=GameInfoDataSchema(game=game_info, heroes=game_heroes, operations=game_operations))
        except HTTPException as e:
            return self.Error(message=str(e))

    async def get_hero_in_game(self, game_id: int) -> HeroesInGameResponceSchema:
        try:
            heroes_in_game = await get_heroes_in_game(self.session, game_id)
            data = [HeroesInGameSchema(**hig) for hig in heroes_in_game]
            return HeroesInGameResponceSchema(data=data)
        except HTTPException as e:
            return self.Error(message=str(e))

    async def set_game_operation(self, request_data: GameOperationRequestSchema) -> StatusSchema:
        try:
            if (request_data.operation < GameOperationsEnum.start.value
                and request_data.operation > GameOperationsEnum.end_time_break.value):
                return self.InvalidRequestParameters()

            await self.session.begin()
            await add_game_opertaion(self.session, request_data.game_id, GameOperationsEnum(request_data.operation), request_data.success_at.replace(tzinfo=None), False)

            if (request_data.operation == GameOperationsEnum.start.value):
                game_start = await update_game_start(self.session, request_data.game_id, request_data.success_at.replace(tzinfo=None), False)
                if (not game_start):
                    await self.session.rollback()
                    return StatusSchema(status='Нет игроков в игре', code=205)
            elif (request_data.operation == GameOperationsEnum.end.value):
                game_end = await update_game_end(self.session, request_data.game_id, request_data.success_at.replace(tzinfo=None), False)
                if (not game_end):
                    await self.session.rollback()
                    return StatusSchema(status='Нет игроков в игре', code=205)
                await move_game_to_history(self.session, request_data.game_id, False)

            await self.session.commit()

            return StatusSchema()
        except HTTPException as e:
            await self.session.rollback()
            return self.Error(message=str(e))

    async def set_rebuy_hero(self, request_data: HeroRequestSchema) -> StatusSchema:
        try:
            current_time = datetime.now(timezone).replace(tzinfo=None)
            if (not await game_is_start(self.session, request_data.game_id)):
                current_time = None
            if (request_data.operation == HeroOpertaionsEnum.rebuy.value):
                await add_game_hero(self.session, request_data.game_id, request_data.hero_id, current_time)
            elif (request_data.operation == HeroOpertaionsEnum.end_game.value):
                await update_game_hero_state(self.session, request_data.game_id, request_data.hero_id, None, current_time)
            else:
                return self.InvalidRequestParameters()

            return StatusSchema()
        except HTTPException as e:
            return self.Error(message=str(e))

    async def set_new_game(self, request_data: NewGameRequestSchema) -> NewGameResponceSchema:
        try:
            if (request_data.tournament_id < 1):
                return self.InvalidRequestParameters()
            game_id = await create_new_game(self.session, request_data.tournament_id)
            return NewGameResponceSchema(game_id=game_id)
        except HTTPException as e:
            return self.Error(message=str(e))
