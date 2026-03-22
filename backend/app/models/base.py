'''
Base для всех моделей + engine

'''

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# Базовый класс для моделей БД
class Base(DeclarativeBase):
    pass


# Cоздаём асинхронный движок для PSQL
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG # Для логов SQL в проде False
)

# Фабрика сессий для пула соединений
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession, # Используем AsyncSession
    expire_on_commit=False # Не истекаем объекты после коммита
)

# Экспортируем для импорта
__all__ = ["Base", "engine", "AsyncSessionLocal"]