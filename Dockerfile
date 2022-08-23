FROM python:3.10.5-slim
RUN apt-get update
RUN apt-get install --no-install-recommends -y \
    python3-dev \
    build-essential \
    libpq-dev \
    gcc \
    openssh-client \
    git

WORKDIR /app
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
