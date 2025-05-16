from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker, AsyncAttrs
from config import settings    


async_engine = create_async_engine(settings.get_db_url(), echo=False)

session_async = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True # класс абстрактный


async def get_db():
    db = session_async()
    try:
        yield db
    finally:
        await db.close()



