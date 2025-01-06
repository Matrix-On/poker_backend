from .types import *
from .history_games import HistoryGames
from core.enums import GameOperations

class HistoryGameOperations(Base):
    __tablename__ = 'history_game_operations'

    id: int = Column(Integer, primary_key=True, index=True, autoincremented=True)
    history_game_id: int = Column(Integer, index=True)
    operation: GameOperations = Column("operation", Enum(GameOperations))
    success_at: datetime = Column(DateTime, default=datetime.utcnow)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    history_games: Mapped[HistoryGames] = relationship(HistoryGames)
