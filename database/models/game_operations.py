from .types import *
from .games import Games
from core.enums import GameOperationsEnum

class GameOperations(Base):
    __tablename__ = 'game_operations'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    game_id: int = Column(Integer, ForeignKey('games.id'), index=True, nullable=False)
    operation: GameOperationsEnum = Column("operation", Enum(GameOperationsEnum), nullable=False)
    success_at: datetime = Column(DateTime, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone()).replace(tzinfo=None), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.now(timezone()).replace(tzinfo=None), onupdate=datetime.now(timezone()).replace(tzinfo=None), nullable=False)

    games: Mapped[Games] = relationship(Games)
