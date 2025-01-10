from sqlalchemy import text, RowMapping, Sequence, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from datetime import datetime

from .models.tournaments import Tournaments
from .models.game_heroes import GameHeroes, Heroes
from .models.game_operations import GameOperations, Games
from .models.history_game_operations import HistoryGameOperations, HistoryGames
from .models.history_game_heroes import HistoryGameHeroes
from core.enums import GameOperationsEnum

async def get_tournaments(session: AsyncSession):
    query = select(Tournaments)
    result = await session.execute(query)
    tournaments = result.fetchall()
    return tournaments

async def get_heroes(session: AsyncSession):
    query = select(Heroes).order_by(Heroes.id)
    result = await session.execute(query)
    heroes = result.fetchall()
    return heroes

async def get_heroes_in_game(session: AsyncSession, game_id: int):
    query = text('SELECT h.id as id, MAX(fullname) as fullname,'
                 ' MIN(started_at) as started_at, count(h.id) as count_rebuy,'
                 ' CASE WHEN COUNT(ended_at) < COUNT(*) THEN NULL ELSE MAX(ended_at) END as ended_at'
                 ' FROM game_heroes gh'
                 ' INNER JOIN heroes h ON (h.id=gh.hero_id) '
                 f' WHERE gh.game_id={game_id}'
                 ' GROUP BY h.id'
                 ' ORDER BY h.id ASC'
                 )
    result = await session.execute(query)
    result = result.mappings().all()
    return result

async def active_games(session: AsyncSession) -> Sequence[RowMapping]:
    query = text(f'SELECT gs.id, name, started_at, price_rebuy, chip_count, level_minutes, break_minutes FROM games gs INNER JOIN tournaments ts ON (gs.tournament_id=ts.id)')
    result = await session.execute(query)
    result = result.mappings().all()
    return result

async def get_game_info(session: AsyncSession, game_id: int):
    query = text('SELECT gs.id, name, started_at, price_rebuy,'
                 ' chip_count, level_minutes, break_minutes '
                 ' FROM games gs'
                 ' INNER JOIN tournaments ts ON (gs.tournament_id=ts.id) '
                 f' WHERE gs.id={game_id}'
                 )
    result = await session.execute(query)
    result = result.mappings().first()
    return result

async def get_blinds_info(session: AsyncSession, game_id: int):
    query = text('SELECT RANK() OVER (ORDER BY big_blind ASC) as level,'
                 ' small_blind, big_blind, ante'
                 ' FROM games gs'
                 ' INNER JOIN tournament_blinds tsbs ON (tsbs.tournament_id=gs.tournament_id) '
                 ' INNER JOIN blinds bs ON (tsbs.blind_id=bs.id) '
                 f' WHERE gs.id={game_id}'
                 ' ORDER BY big_blind ASC'
                 )
    result = await session.execute(query)
    result = result.mappings().all()
    return result

async def get_game(session: AsyncSession, game_id: int) -> Games | None:
    game = await session.get(Games, game_id)
    return game

async def get_tournament(session: AsyncSession, tournament_id: int):
    tournament = await session.get(Tournaments, tournament_id)
    return tournament

async def get_game_heroes(session: AsyncSession, game_id: int):
    query = select(GameHeroes).options(selectinload(GameHeroes.heroes)).where(GameHeroes.game_id==game_id).order_by(GameHeroes.started_at)
    result = await session.execute(query)
    game_heroes = result.fetchall()
    return game_heroes

async def get_game_operations(session: AsyncSession, game_id: int):
    query = select(GameOperations).where(GameOperations.game_id==game_id).order_by(GameOperations.success_at)
    result = await session.execute(query)
    game_operations = result.fetchall()
    return game_operations

async def create_new_game(session: AsyncSession, tournament_id: int) -> int:
    game = Games()
    game.tournament_id = tournament_id
    session.add(game)
    await session.commit()
    return game.id

async def update_game_hero_state(session: AsyncSession, game_id: int, hero_id: int, started_at: datetime | None, ended_at: datetime | None):
    query = select(GameHeroes).where(GameHeroes.game_id==game_id,
                                     GameHeroes.hero_id==hero_id,
                                     GameHeroes.ended_at==None)
    result = await session.execute(query)
    game_heroes = result.scalar()
    if (not game_heroes):
        return
    if (started_at):
        game_heroes.started_at=started_at.replace(tzinfo=None)
    if (ended_at):
        game_heroes.ended_at=ended_at.replace(tzinfo=None)

    await session.commit()

async def add_game_hero(session: AsyncSession, game_id: int, hero_id: int, started_at: datetime | None):
    game_hero = GameHeroes()
    game_hero.game_id = game_id
    game_hero.hero_id = hero_id
    if (started_at):
        game_hero.started_at = started_at.replace(tzinfo=None)
    session.add(game_hero)
    await session.commit()
    return game_hero.id

async def game_is_start(session: AsyncSession, game_id: int) -> bool:
    query = select(Games).where(Games.id==game_id)
    result = await session.execute(query)
    game = result.scalar()
    if (not game or not game.started_at):
        return False
    return True

async def update_game_start(session: AsyncSession, game_id: int, started_at: datetime, commit: bool = True) -> bool:
    query = select(GameHeroes).options(selectinload(GameHeroes.games)).where(GameHeroes.game_id==game_id)
    result = await session.execute(query)
    game_heroes = result.scalars().all()
    if (len(game_heroes) == 0):
        return False
    game_heroes[0].games.started_at=started_at
    for hero in game_heroes:
        if not hero.started_at:
            hero.started_at=started_at
    if commit:
        await session.commit()
    return True

async def update_game_end(session: AsyncSession, game_id: int, ended_at: datetime, commit: bool = True) -> bool:
    query = select(GameHeroes).options(selectinload(GameHeroes.games)).where(GameHeroes.game_id==game_id)
    result = await session.execute(query)
    game_heroes = result.scalars().all()
    if (len(game_heroes) == 0):
        return False
    game_heroes[0].games.ended_at=ended_at
    for hero in game_heroes:
        if not hero.ended_at:
            hero.ended_at=ended_at
    if commit:
        await session.commit()
    return True

async def add_game_opertaion(session: AsyncSession, game_id: int, opertaion: GameOperationsEnum, success_at: datetime, commit: bool = True) -> int:
    game_operation = GameOperations()
    game_operation.game_id = game_id
    game_operation.operation = opertaion
    game_operation.success_at = success_at
    session.add(game_operation)
    if commit:
        await session.commit()
    return game_operation.id

async def get_game_operation_objects(session: AsyncSession, game_id: int) -> Sequence[GameOperations]:
    query = select(GameOperations).where(GameOperations.game_id==game_id)
    result = await session.execute(query)
    game_operations = result.scalars().all()
    return game_operations

async def get_game_heroes_objects(session: AsyncSession, game_id: int) -> Sequence[GameHeroes]:
    query = select(GameHeroes).where(GameHeroes.game_id==game_id)
    result = await session.execute(query)
    game_heroes = result.scalars().all()
    return game_heroes

async def get_game_objets(session: AsyncSession, game_id: int) -> Games:
    query = select(Games).options(selectinload(Games.tournaments)).where(Games.id==game_id)
    result = await session.execute(query)
    game = result.scalar()
    return game

async def get_win_hero_id(session: AsyncSession, game_id: int) -> int:
    query = select(GameHeroes).where(GameHeroes.game_id==game_id).order_by(desc(GameHeroes.ended_at)).limit(1)
    result = await session.execute(query)
    game_heroe = result.scalar()
    return game_heroe.hero_id

async def move_game_to_history(session: AsyncSession, game_id: int, commit: bool = True) -> int:
    game = await get_game_objets(session, game_id)
    game_heroes = await get_game_heroes_objects(session, game_id)

    history_game = HistoryGames()
    history_game.tournament_id = game.tournament_id
    history_game.started_at = game.started_at
    history_game.ended_at = game.ended_at
    history_game.win_hero_id = await get_win_hero_id(session, game_id)
    history_game.win_total = len(game_heroes) * game.tournaments.price_rebuy
    session.add(history_game)

    game_operations = await get_game_operation_objects(session, game_id)
    for g_o in game_operations:
        history_game_opertaions = HistoryGameOperations()
        history_game_opertaions.history_game_id = history_game.id
        history_game_opertaions.operation = g_o.operation
        history_game_opertaions.success_at = g_o.success_at
        await session.delete(g_o)
        session.add(history_game_opertaions)

    for g_h in game_heroes:
        history_game_heroes = HistoryGameHeroes()
        history_game_heroes.history_game_id = history_game.id
        history_game_heroes.hero_id = g_h.hero_id
        history_game_heroes.started_at = g_h.started_at
        history_game_heroes.ended_at = g_h.ended_at
        await session.delete(g_h)
        session.add(history_game_heroes)


    await session.delete(game)
    if (commit):
        session.commit()
    return history_game.id
