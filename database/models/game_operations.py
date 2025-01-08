from .types import *
from .games import Games
from core.enums import GameOperations

class GameOperations(Base):
    __tablename__ = 'game_operations'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_id: int = Column(Integer, ForeignKey('games.id'), index=True, nullable=False)
    operation: GameOperations = Column("operation", Enum(GameOperations), nullable=False)
    success_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    games: Mapped[Games] = relationship(Games)
