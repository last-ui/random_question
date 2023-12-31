from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app.core.config import settings

Base = declarative_base()

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)
