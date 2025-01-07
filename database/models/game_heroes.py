from .types import *
from .games import Games
from .heroes import Heroes

class GameHeroes(Base):
    __tablename__ = 'game_heroes'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_id: int = Column(Integer, index=True, nullable=False)
    hero_id: int = Column(Integer, index=True, nullable=False)
    started_at: datetime = Column(DateTime, default=datetime.utcnow)
    ended_at: datetime = Column(DateTime, default=datetime.utcnow)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    games: Mapped[Games] = relationship(Games)
    heroes: Mapped[Heroes] = relationship(Heroes)
