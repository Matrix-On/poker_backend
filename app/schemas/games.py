from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime
from .base import StatusSchema

class ActiveGamesSchema(BaseModel):
    id: int
    name: str
    started_at: datetime
    price_rebuy: int
    chip_count: int
    level_minutes: int
    break_minutes: int

class ActiveGamesResponceSchema(StatusSchema):
    data: List[ActiveGamesSchema]

class HeroesSchema(BaseModel):
    id: int
    fullname: str
    started_at: datetime
    ended_at: datetime

class OperationsSchema(BaseModel):
    id: int
    operation: int
    success_at: datetime

class GameInfoResponceSchema(StatusSchema):
    heroes: List[HeroesSchema]
    operations: List[OperationsSchema]
    tournament: ActiveGamesSchema

class GameOperationRequestSchema(BaseModel):
    operation: int
    success_at: datetime

class HeroRequestSchema(BaseModel):
    hero_id: int
    operation_datetime: datetime
