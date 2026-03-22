from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ProductCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=100, description="Артикул маркетплейса")
    name: str = Field(max_length=255, description="Наименование товара")
    ean: str = Field(min_length=1, max_length=20, description="Штрихкод EAN")
    category: Optional[str] = Field(None, max_length=100, description="Категория товара")
    vendor: Optional[str] = Field(None, max_length=100, description="Бренд/производитель")
    price: float = Field(gt=0, description="Цена в кабинете")
    cost_price: Optional[float] = Field(None, ge=0, description="Себестоимость")

class ProductOut(ProductCreate):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
