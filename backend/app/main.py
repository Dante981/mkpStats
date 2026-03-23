#uvicorn main:app --reload

from fastapi import (
    FastAPI,
    Depends,
    HTTPException
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.routers import product

app = FastAPI(title="Unit Econ MVP")

app.include_router(product.router, prefix="/api/v1", tags=["products"])


@app.get("/")
async def root():
    return {"message": "Unit Economics API MVP готов!"}