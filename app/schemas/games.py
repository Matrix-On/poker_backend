from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime
from .base import StatusSchema

class ActiveGamesSchema(BaseModel):
    id: int
    name: str
    started_at: datetime | None
    price_rebuy: int
    chip_count: int
    level_minutes: int
    break_minutes: int

class ActiveGamesResponceSchema(StatusSchema):
    data: List[ActiveGamesSchema]

class HeroesSchema(BaseModel):
    id: int
    fullname: str
    started_at: datetime | None
    ended_at: datetime | None

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

class GameInfoResponceSchema(StatusSchema):
    heroes: List[HeroesSchema]
    operations: List[OperationsSchema]
    game: GameInfoSchema

class GameOperationRequestSchema(BaseModel):
    game_id: int
    operation: int
    success_at: datetime

class HeroRequestSchema(BaseModel):
    game_id: int
    hero_id: int
    operation: int
    operation_datetime: datetime

class NewGameRequestSchema(BaseModel):
    tournament_id: int

class NewGameResponceSchema(StatusSchema):
    game_id: int
