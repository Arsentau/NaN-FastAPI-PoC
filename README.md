# NaN-Labs - FastAPI - PoC

## Prerequisites
- Python 3.10
- Docker 20.10
- Docker Compose 2.6

## Create venv
To create a Native Python virtual environment simply run the following command on the project's folder:

`python -m venv .venv --prompt fastapi`

## Install dependencies
Be sure you have the virtual environment active.
If not in the root folder of the project execute:
`source .venv/bin/activate`

Once the virtual environment is activated run:
`pip install -r requirements.txt`

## Add .env file
In the root directory of the project create a `.env` file with the following fields:
```
TITLE=Title
VERSION=0.0.1
DEBUG=True
HOST=0.0.0.0
PORT=8000
ALLOW_ORIGINS='["*"]'
ALLOW_CREDENTIALS='["*"]'
ALLOW_METHODS='["*"]'
ALLOW_HEADERS='["*"]'
```
If this file is not added the project will use default variables to allow you run the application by default.

## Add .env.database
This file is required to run the dockerized Database.
In the root directory of the project create a `.env.database` file with the following fields:
```
POSTGRES_HOST=nan-fastapi-poc-db-1
POSTGRES_PORT=5432
POSTGRES_USER=fastapi
POSTGRES_PASSWORD=fastapi
POSTGRES_NAME=fastapi
PGADMIN_DEFAULT_EMAIL=fastapi@localhost.com
PGADMIN_DEFAULT_PASSWORD=fastapi
```
**IMPORTANT** The value of `POSTGRES_HOST` should be the name of the db container.
**These values can be directly used.**

# How to run locally
- Open your terminal on the root project directory
- Run the command `docker-compose up --build`
- To see docs ands schemas you can access
    - OpenApi documentation
    ```bash
    http://0.0.0.0:8000/docs#/
    ```
    - ReDoc documentation:
    ```bash
    http://0.0.0.0:8000/redoc
    ```

---

# How to create development environment

## First
- Complete the following steps described at the beginning of this file:
   - Create venv
   - Install dependencies
   - Add .env file
   - Add .env.database file

## Install pre-commit
To install pre-commit in the .git hooks folder you only need to run the following command in the root folder of the project:

```bash
pre-commit install
```

## Apply last committed migration
- To run the last migration run the following command:

```bash
alembic upgrade head
```
## Create migration

```bash
alembic revision --autogenerate -m "<message>"
```

## Apply migration
- In order to apply the last committed revision execute the following command:
```bash
alembic upgrade head
```

- To apply one specific revision execute this command
```bash
alembic upgrade <revision_code>
```
