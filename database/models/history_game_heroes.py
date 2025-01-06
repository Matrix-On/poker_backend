from .types import *
from .history_games import HistoryGames
from .heroes import Heroes

class HistoryGameHeroes(Base):
    __tablename__ = 'history_game_heroes'

    id: int = Column(Integer, primary_key=True, index=True, autoincremented=True)
    history_game_id: int = Column(Integer, index=True)
    hero_id: int = Column(Integer, index=True)
    started_at: datetime = Column(DateTime, default=datetime.utcnow)
    ended_at: datetime = Column(DateTime, default=datetime.utcnow)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    games: Mapped[HistoryGames] = relationship(HistoryGames)
    heroes: Mapped[Heroes] = relationship(Heroes)
