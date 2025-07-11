from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Optional

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings  # Assuming settings is defined in app/core/config.py

Base = declarative_base()

DATABASE_URL = settings.DATABASE_URL


# @logger
class Database:
    """
    Database connection manager using SQLAlchemy with asynchronous support.

    This class initializes an asynchronous database engine and session factory
    for managing database interactions.

    Attributes:
        _engine: The asynchronous database engine created using `create_async_engine`.
        _session_factory: A session factory using `sessionmaker` to generate async sessions.

    Methods:
        db_connection(): Provides an asynchronous database session using a context manager.
    """
    def __init__(self) -> None:
        self._engine = create_async_engine(
            DATABASE_URL,# Database connection URL
            echo=True, # Enables logging of SQL queries for debugging
            future=True
        )
        self._session_factory = sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False
        )


    @asynccontextmanager
    async def db_connection(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Provide a transactional scope around a series of operations.
        This method yields a database session for use in context managers.
        """
        async with self._session_factory() as session:
            try:
                yield session
            except Exception as e:
                print("eeeee>>>>", e)
            finally:
                await session.close()


    def close(self) -> None:
        """
        Closes all sessions in the session factory.
        """
        self._session_factory.close_all()


    async def execute_procedure(self, query: str, params: dict) -> Optional[Any]:
        """
        Executes a stored procedure with the provided query and parameters.
        """
        try:
            async with self._engine.begin() as conn:
                result = await conn.execute(text(query), params)
                return result
        except Exception as e:
            raise ValueError
