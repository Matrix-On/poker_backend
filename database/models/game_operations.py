from .types import *
from .games import Games
from core.enums import GameOperations

class GameOperations(Base):
    __tablename__ = 'game_operations'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_id: int = Column(Integer, index=True)
    operation: GameOperations = Column("operation", Enum(GameOperations))
    success_at: datetime = Column(DateTime, default=datetime.utcnow)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    games: Mapped[Games] = relationship(Games)
