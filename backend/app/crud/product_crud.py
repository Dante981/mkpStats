from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.product import Product
from app.schemas.product import ProductCreate


async def create_product(product_in: ProductCreate, db: AsyncSession) -> Product:
    product = Product(**product_in.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def get_product(sku: str, db: AsyncSession) -> Product:
    result = await db.execute(select(Product).where(Product.sku == sku))
    return result.scalar_one_or_none()