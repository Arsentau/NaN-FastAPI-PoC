FROM python:3.10.5-slim

WORKDIR /app

# Install dependencies

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
