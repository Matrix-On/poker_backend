from .types import *
from .history_games import HistoryGames
from .heroes import Heroes

class HistoryGameHeroes(Base):
    __tablename__ = 'history_game_heroes'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    history_game_id: int = Column(Integer, index=True, nullable=False)
    hero_id: int = Column(Integer, index=True, nullable=False)
    started_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    ended_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    games: Mapped[HistoryGames] = relationship(HistoryGames)
    heroes: Mapped[Heroes] = relationship(Heroes)
