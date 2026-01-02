from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from typing import AsyncGenerator
from .logging import get_logger
from .config import settings


logger = get_logger()

engine = create_async_engine(url=settings.POSTGRES_URL)

SessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False, echo=settings.DEBUG
)


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with SessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"An Error ocuured while getting session for db :  {e}")
            await session.rollback()
            raise
        finally:
            await session.close()

async def init_db():
    pass