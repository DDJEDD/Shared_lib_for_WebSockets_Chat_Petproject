from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

class DB:
    '''
    Database class
    This class is used to
    initialize the database
    and create a session
    '''
    def __init__(self, database_url: str):
        self.database_url = database_url

        self.engine = create_async_engine(
            self.database_url,
            pool_pre_ping=True,
        )

        self.SessionLocal = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.SessionLocal() as session:
            yield session