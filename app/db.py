from sqlalchemy import Column, Text, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from .configs import DATABASE_URL
import uuid
from sqlalchemy.dialects.postgresql import UUID


engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
print(DATABASE_URL)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session

