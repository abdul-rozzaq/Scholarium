FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    tree \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements /app/requirements

RUN pip install --no-cache-dir -r requirements/prod.txt

COPY . .
