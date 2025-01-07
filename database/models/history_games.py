from .types import *
from .tournaments import Tournaments
from .heroes import Heroes

class HistoryGames(Base):
    __tablename__ = 'history_games'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tournament_id: int = Column(Integer, index=True)
    win_hero_id: int = Column(Integer, index=True)
    win_total: int = Column(Integer)
    started_at: datetime = Column(DateTime, default=datetime.utcnow)
    ended_at: datetime = Column(DateTime, default=datetime.utcnow)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tournaments: Mapped[Tournaments] = relationship(Tournaments)
    heroes: Mapped[Heroes] = relationship(Heroes)
