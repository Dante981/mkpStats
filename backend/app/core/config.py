'''
Загрузка переменных окружения .env

DATABASE_URL: str - URL подключения к PostgreSQL с asyncpg драйвером

REDIS_URL: str - Секретный ключ для JWT токенов

ALGORITHM: str = "HS256" - Алгоритм подписи JWT

ACCESS_TOKEN_EXPIRE_MINUTES: int =  - Время жизни access токена в минутах

env_file = ".env" - путь к файлу

'''


from pydantic_settings import BaseSettings
from typing import Optional


# Класс настроек наследуется от BaseSettings - автоматически загружает .env
class Settings(BaseSettings):
    # URL подключения к PostgreSQL с asyncpg драйвером
    DATABASE_URL: str
    DATABASE_URL_SYNC: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    # URL Redis брокера для Celery
    REDIS_URL: str
    DEBUG: bool
    # Секретный ключ для JWT токенов
    SECRET_KEY: str
    # Алгоритм подписи JWT
    ALGORITHM: str = "HS256"
    # Время жизни access токена в минутах
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        # Указываем откуда брать .env файл
        env_file = ".env"

# Создаем глобальный экземпляр настроек
settings = Settings()