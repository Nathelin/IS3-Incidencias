FROM python:3.13-alpine

RUN apk add --no-cache \
    gcc musl-dev libffi-dev python3-dev \
    postgresql-dev jpeg-dev zlib-dev \
    libjpeg

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["python", "api/manage.py", "runserver", "0.0.0.0:8000"]
