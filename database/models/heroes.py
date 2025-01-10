from .types import *

class Heroes(Base):
    __tablename__ = 'heroes'

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullname: str = Column(String, nullable=False)
    total_win: int = Column(Integer, default=0, nullable=False)
    total_lose: int = Column(Integer, default=0, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.now(timezone).replace(tzinfo=None), onupdate=datetime.now(timezone).replace(tzinfo=None), nullable=False)
