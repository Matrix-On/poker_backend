from .types import *
from .tournaments import Tournaments

class Games(Base):
    __tablename__ = 'games'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tournament_id: int = Column(Integer, index=True)
    started_at: datetime = Column(DateTime, default=datetime.utcnow)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tournaments: Mapped[Tournaments] = relationship(Tournaments)
