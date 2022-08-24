FROM python:3.10.5-slim

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
    python3-dev \
    build-essential \
    libpq-dev \
    gcc \
    openssh-client \
    git
RUN python3 -m pip install --upgrade pip

WORKDIR /app/src

COPY ./requirements.txt /app
RUN python3 -m pip install -r ../requirements.txt
COPY ./entrypoint.sh /app/src
COPY ./src /app/src
COPY .env /app/src/
COPY .env.database /app/src/
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
