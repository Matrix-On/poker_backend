from .types import *
from .games import Games
from .heroes import Heroes

class GameHeroes(Base):
    __tablename__ = 'game_heroes'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_id: int = Column(Integer, ForeignKey('games.id'), index=True, nullable=False)
    hero_id: int = Column(Integer, ForeignKey('heroes.id'), index=True, nullable=False)
    started_at: datetime = Column(DateTime)
    ended_at: datetime = Column(DateTime)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone()).replace(tzinfo=None), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.now(timezone()).replace(tzinfo=None), onupdate=datetime.now(timezone()).replace(tzinfo=None), nullable=False)

    games: Mapped[Games] = relationship(Games)
    heroes: Mapped[Heroes] = relationship(Heroes)
