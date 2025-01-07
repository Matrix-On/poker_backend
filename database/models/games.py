from .types import *
from .tournaments import Tournaments

class Games(Base):
    __tablename__ = 'games'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tournament_id: int = Column(Integer, index=True, nullable=False)
    started_at: datetime = Column(DateTime, default=datetime.utcnow)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    tournaments: Mapped[Tournaments] = relationship(Tournaments)
