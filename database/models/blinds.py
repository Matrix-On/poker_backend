from .types import *

class Blinds(Base):
    __tablename__ = 'blinds'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    small_blind: int = Column(Integer, default=0, nullable=False)
    big_blind: int = Column(Integer, default=0, nullable=False)
    ante: int = Column(Integer, default=0, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
