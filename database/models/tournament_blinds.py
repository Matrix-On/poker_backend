from .types import *
from .blinds import Blinds
from .tournaments import Tournaments

class TournamentBlinds(Base):
    __tablename__ = 'tournament_blinds'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tournament_id: int = Column(Integer, index=True)
    blind_id: int = Column(Integer, index=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tournaments: Mapped[Tournaments] = relationship(Tournaments)
    blind: Mapped[Blinds] = relationship(Blinds)
