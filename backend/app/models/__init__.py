from .base import (
    Base,
    engine,
    AsyncSessionLocal
)

from .product import Product


# Экспортируем для удобства
__all__ = [
    "Base", "engine", "AsyncSessionLocal",
    "Product",
]


Base.metadata  # Alembic сканирует все модели здесь