from sqlalchemy import text, RowMapping, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models.tournaments import Tournaments
from .models.game_heroes import GameHeroes
from .models.game_operations import GameOperations, Games

async def active_games(session: AsyncSession) -> Sequence[RowMapping]:
    query = text(f'SELECT gs.id, name, started_at, price_rebuy, chip_count, level_minutes, break_minutes FROM games gs INNER JOIN tournaments ts ON (gs.tournament_id=ts.id) WHERE gs.id=33')
    result = await session.execute(query)
    result = result.mappings().all()
    return result

async def get_game_info(session: AsyncSession, game_id: int):
    query = text(f'SELECT gs.id, name, started_at, price_rebuy, chip_count, level_minutes, break_minutes FROM games gs INNER JOIN tournaments ts ON (gs.tournament_id=ts.id) WHERE gs.id={game_id}')
    result = await session.execute(query)
    result = result.mappings().first()
    return result

async def get_game(session: AsyncSession, game_id: int) -> Games | None:
    game = await session.get(Games, game_id)
    return game

async def get_tournament(session: AsyncSession, tournament_id: int):
    tournament = await session.get(Tournaments, tournament_id)
    return tournament

async def get_game_heroes(session: AsyncSession, game_id: int):
    query = select(GameHeroes).where(GameHeroes.id==game_id)
    result = await session.execute(query)
    game_heroes = result.fetchall()
    return game_heroes

async def get_game_operations(session: AsyncSession, game_id: int):
    query = select(GameOperations).where(GameOperations.id==game_id)
    result = await session.execute(query)
    game_operations = result.fetchall()
    return game_operations
