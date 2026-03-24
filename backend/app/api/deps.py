from app.models import engine, AsyncSessionLocal

async def get_db():
    """Dependency для роутеров"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()