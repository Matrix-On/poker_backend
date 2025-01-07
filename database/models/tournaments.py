from .types import *

class Tournaments(Base):
    __tablename__ = 'tournaments'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String)
    price_rebuy: int = Column(Integer, default=0)
    chip_count: int = Column(Integer, default=0)
    level_minutes: int = Column(Integer, default=0)
    break_minutes: int = Column(Integer, default=0)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
