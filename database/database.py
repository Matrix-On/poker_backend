from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import settings



engine = create_async_engine(settings.database_url, echo=True)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency
async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
