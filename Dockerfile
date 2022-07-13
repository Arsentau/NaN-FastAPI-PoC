FROM python:3.10.5

RUN python3 -m pip install --upgrade pip

COPY requirements.txt .

RUN python3 -m  pip install -r requirements.txt

WORKDIR /app

COPY ./ /
