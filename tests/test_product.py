import pytest
from httpx import AsyncClient
from app.main import app
from app.core.config import settings


@pytest.mark.asyncio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http:/test") as ac:
        responce = await ac.post(
            "/api/v1/products/",
            json={
                "sku": "TEST",
                "name": "Test Product",
                "price": 1000
            }
        )
        assert responce.status_code == 200
        data = responce.json()
        assert data['sku'] == "TEST"
        assert data['price'] == 1000