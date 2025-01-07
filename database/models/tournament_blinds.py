from .types import *
from .blinds import Blinds
from .tournaments import Tournaments

class TournamentBlinds(Base):
    __tablename__ = 'tournament_blinds'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tournament_id: int = Column(Integer, index=True, nullable=False)
    blind_id: int = Column(Integer, index=True, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    tournaments: Mapped[Tournaments] = relationship(Tournaments)
    blind: Mapped[Blinds] = relationship(Blinds)
