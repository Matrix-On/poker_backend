from .types import *

class Blinds(Base):
    __tablename__ = 'blinds'

    id: int = Column(Integer, primary_key=True, index=True, autoincremented=True)
    small_blind: int = Column(Integer, default=0)
    big_blind: int = Column(Integer, default=0)
    ante: int = Column(Integer, default=0)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
