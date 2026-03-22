'''
функци get_db - для получения БД сессии(Автоматически открывает/закрывает транзакцию)

'''

from app.models import (
    engine,
    AsyncSessionLocal
)


# Dependency для FastAPI - предоставляет сессию БД в роутерах
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session