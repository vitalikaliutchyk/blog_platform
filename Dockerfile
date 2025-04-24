FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Никакого Gunicorn - используем встроенный сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]