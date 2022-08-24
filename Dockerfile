FROM python:3.10.5-slim
RUN apt-get update
RUN apt-get install --no-install-recommends -y \
    python3-dev \
    build-essential \
    libpq-dev \
    gcc \
    openssh-client \
    git

COPY ./requirements.txt /app/

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
ENTRYPOINT ["./scripts/migrations.sh"]
