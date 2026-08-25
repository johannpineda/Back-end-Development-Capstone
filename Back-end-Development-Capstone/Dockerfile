FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput || true
ENV PORT=8000
CMD ["sh","-c","python manage.py migrate && gunicorn --bind 0.0.0.0:${PORT} bandsite.wsgi:application"]
