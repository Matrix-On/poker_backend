from pydantic import BaseModel
from typing import List
from datetime import datetime
from .base import StatusSchema

class TournamentsSchema(BaseModel):
    id: int
    name: str
    price_rebuy: int
    guaranteed_amount: int
    currency: str
    chip_count: int
    level_minutes: int
    break_minutes: int
    break_after_level: int

class ActiveGamesSchema(TournamentsSchema):
    started_at: datetime | None
    total_chips: int
    total_pot: int
    entries: int
    players_in: int
    level: int

class TournamentsResponceSchema(StatusSchema):
    data: List[TournamentsSchema]

class ActiveGamesResponceSchema(StatusSchema):
    data: List[ActiveGamesSchema]

class HeroesSchema(BaseModel):
    id: int
    fullname: str

class HeroesGameSchema(HeroesSchema):
    started_at: datetime | None
    ended_at: datetime | None

class HeroesResponceSchema(StatusSchema):
    data: List[HeroesSchema]

class OperationsSchema(BaseModel):
    id: int
    operation: int
    success_at: datetime

class BlindsSchema(BaseModel):
    level: int
    small_blind: int
    big_blind: int
    ante: int

class GameInfoSchema(ActiveGamesSchema):
    blinds: List[BlindsSchema]

class GameInfoDataSchema(BaseModel):
    heroes: List[HeroesGameSchema]
    operations: List[OperationsSchema]
    game: GameInfoSchema

class GameInfoResponceSchema(StatusSchema):
    data: GameInfoDataSchema

class GameOperationRequestSchema(BaseModel):
    game_id: int
    operation: int
    success_at: datetime

class HeroRequestSchema(BaseModel):
    game_id: int
    hero_id: int
    operation: int

class NewGameRequestSchema(BaseModel):
    tournament_id: int

class NewGameResponceSchema(StatusSchema):
    game_id: int

class HeroesInGameSchema(HeroesGameSchema):
    count_rebuy: int

class HeroesInGameResponceSchema(StatusSchema):
    data: List[HeroesInGameSchema]
