from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductOut
from app.crud import product_crud



router = APIRouter()

@router.post("/products/", response_model=ProductOut)
async def create_product(
    product_in: ProductCreate,
    db: AsyncSession = Depends(get_db)
):

    existing = await product_crud.get_product(product_in.sku, db) 
    if existing:
        raise HTTPException(status_code=400, detail="SKU уже существует")
    return await product_crud.create_product(product_in, db)

@router.get("/products/{sku}", response_model=ProductOut)
async def read_product(sku: str, db: AsyncSession = Depends(get_db)):
    product = await product_crud.get_product(sku, db)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product