from config.settings import get_settings
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool

settings = get_settings()

engine = create_async_engine(settings.DATABASE_URI, poolclass=NullPool)

SessionLocal = async_sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


async def get_session() -> AsyncGenerator:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    session = SessionLocal()
    try:
        yield session
    except Exception as exc:
        print(exc.args)
        await session.rollback()
    finally:
        await session.close()
