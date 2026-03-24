FROM python:3.11-slim AS builder

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN set -x && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем alembic.ini ДО COPY . 
COPY alembic.ini .

# Копируем код
COPY . .

# =========================================
FROM python:3.11-slim

WORKDIR /app

# Копируем Python пакеты ИЗ builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Копируем alembic.ini ИЗ builder
COPY --from=builder /app/alembic.ini /app/alembic.ini

# Копируем остальной код
COPY --from=builder /app /app

EXPOSE 8000

# ПОРТ 8000 (было 8800!)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
