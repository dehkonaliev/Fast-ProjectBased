from sqlalchemy import Column, Text, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

import uuid
from sqlalchemy.dialects.postgresql import UUID

DATA_BASE_URL = ""