from .types import *
from .history_games import HistoryGames
from core.enums import GameOperations

class HistoryGameOperations(Base):
    __tablename__ = 'history_game_operations'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    history_game_id: int = Column(Integer, index=True, nullable=False)
    operation: GameOperations = Column("operation", Enum(GameOperations), nullable=False)
    success_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    history_games: Mapped[HistoryGames] = relationship(HistoryGames)
