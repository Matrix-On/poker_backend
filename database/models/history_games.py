from .types import *
from .tournaments import Tournaments
from .heroes import Heroes

class HistoryGames(Base):
    __tablename__ = 'history_games'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tournament_id: int = Column(Integer, ForeignKey('tournaments.id'), index=True, nullable=False)
    win_hero_id: int = Column(Integer, ForeignKey('heroes.id'), index=True, nullable=False)
    win_total: int = Column(Integer, nullable=False)
    started_at: datetime = Column(DateTime, nullable=False)
    ended_at: datetime = Column(DateTime, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), onupdate=datetime.now(timezone).replace(tzinfo=None), nullable=False)

    tournaments: Mapped[Tournaments] = relationship(Tournaments)
    heroes: Mapped[Heroes] = relationship(Heroes)
