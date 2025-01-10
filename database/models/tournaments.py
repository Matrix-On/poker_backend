from .types import *

class Tournaments(Base):
    __tablename__ = 'tournaments'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    price_rebuy: int = Column(Integer, default=0, nullable=False)
    chip_count: int = Column(Integer, default=0, nullable=False)
    level_minutes: int = Column(Integer, default=0, nullable=False)
    break_minutes: int = Column(Integer, default=0, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), onupdate=datetime.now(timezone).replace(tzinfo=None), nullable=False)
