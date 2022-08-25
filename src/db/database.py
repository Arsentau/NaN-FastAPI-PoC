from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import DbSettings, Settings

# Get DB credentials from .env.database file
DB_CREDENTIALS: DbSettings = Settings.get_db_settings()

SQLALCHEMY_DATABASE_URL = "postgresql://%s:%s@%s:%s/%s" % (
    DB_CREDENTIALS.postgres_user,
    DB_CREDENTIALS.postgres_password,
    DB_CREDENTIALS.postgres_host,
    DB_CREDENTIALS.postgres_port,
    DB_CREDENTIALS.postgres_name
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
