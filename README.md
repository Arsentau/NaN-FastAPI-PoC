# NaN-Labs - FastAPI - PoC

## Prerequisites
- Python 3.10
- Docker 20.10
- Docker Compose 2.6

## Create venv
To create a Native Python virtual environment simply run the following command on the project's folder:

`python -m venv .venv --prompt fastapi`

## Add .env file
In the root directory of the project create a `.env` file with the following fields:
```
TITLE=Title
VERSION=0.0.1
DEBUG=True
HOST=localhost
PORT=8000
ALLOW_ORIGINS=[*]
ALLOW_CREDENTIALS=[*]
ALLOW_METHODS=[*]
ALLOW_HEADERS=[*]
```
If this file is not added the project will use default variables to allow you run the application by default.

## Add .env.database
This file is required to run the dockerized Database.
In the root directory of the project create a `.env` file with the following fields:
```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=fastapi
POSTGRES_PASSWORD=fastapi
POSTGRES_NAME=fastapi
PGADMIN_DEFAULT_EMAIL=fastapi@localhost.com
PGADMIN_DEFAULT_PASSWORD=fastapi
```
**This values can be directly used.**

## How to run locally
- Open your terminal on the root project directory
- Run the command `docker compose up --build`
- To see docs ands schemas you can access
    - OpenApi documentation
    ```bash
    http://0.0.0.0:8000/docs#/
    ```
    - ReDoc documentation:
    ```bash
    http://0.0.0.0:8000/redoc
    ```
