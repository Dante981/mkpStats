FROM python:3.11-slim AS builder

# Рабочая директория
WORKDIR /app


# Копируем только requirements.txt 
COPY requirements.txt .

# Устанавливаем зависимости БЕЗ кэша
RUN set -x && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


FROM python:3.11-slim

# Копируем установленные пакеты из builder 
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin


# Рабочая директория приложения
WORKDIR /app

# Копируем ВЕСЬ код проекта
COPY . .

# Открываем порт 8000 для FastAPI
EXPOSE 8000

# Запуск uvicorn с hot-reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8800", "--reload"]