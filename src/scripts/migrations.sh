#!/bin/sh

alembic -c alembic.ini upgrade head

uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug --reload