from .types import *

class Heroes(Base):
    __tablename__ = 'heroes'

    id: int = Column(Integer, primary_key=True, index=True, autoincremented=True)
    fullname: str = Column(String)
    total_win: int = Column(Integer, default=0)
    total_lose: int = Column(Integer, default=0)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
