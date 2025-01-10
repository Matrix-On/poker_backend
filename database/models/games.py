from .types import *
from .tournaments import Tournaments

class Games(Base):
    __tablename__ = 'games'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tournament_id: int = Column(Integer, ForeignKey('tournaments.id'), index=True, nullable=False)
    started_at: datetime = Column(DateTime)
    ended_at: datetime = Column(DateTime)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), onupdate=datetime.now(timezone).replace(tzinfo=None), nullable=False)

    tournaments: Mapped[Tournaments] = relationship(Tournaments)
