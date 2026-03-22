'''
Модель для карточек товара

id - индификатор в БД [BigInteger, primary_key=True, index=True]
sku - артикул маркетплейса [String(100), unique=True, index=True, nullable=False]
name - наименование [String(255), nullable=False]
ean - штрихкод [String(20), unique=True, index=True, nullable=False]
category - категория [String(100), index=True]
vendor - бренд [String(100)]
price - цена в кабинете [Float, nullable=False]
cost_price - себестоймость [[Float]]

created_at - дата создания [DateTime, default=func.now()]

'''

from .base import Base
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Float,
    DateTime,
    func,
    Index
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from typing import List
from datetime import datetime

class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    ean: Mapped[str] = mapped_column(String(20))
    category: Mapped[str] = mapped_column(String(100), index=True)
    vendor: Mapped[str] = mapped_column(String(100), index=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    cost_price: Mapped[float] = mapped_column(Float)

    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    __table_args__ = (Index('ix_products_category_vendor', 'category', 'vendor'),)