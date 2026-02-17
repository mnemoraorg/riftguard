from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from src.config.env import settings

# Create Async Engine
engine = create_async_engine(settings.DATABASE_URL, echo=False)

# Session Factory
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Base class for ORM models
class Base(DeclarativeBase):
    pass

async def get_db():
    """Dependency for getting async session"""
    async with AsyncSessionLocal() as session:
        yield session
