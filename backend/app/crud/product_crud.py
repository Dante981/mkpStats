from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.product import Product
from app.schemas.product import ProductCreate
from typing import List

async def create_product(product_in: ProductCreate, db: AsyncSession) -> Product:
    product = Product(**product_in.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def get_product(sku: str, db: AsyncSession) -> Product:
    result = await db.execute(select(Product).where(Product.sku == sku))
    return result.scalar_one_or_none()

async def get_all_products(db: AsyncSession) -> List[Product]:
    result = await db.execute(select(Product))
    return result.scalars().all()