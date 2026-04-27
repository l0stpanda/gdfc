from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./gdfc.db")

engine = create_engine(
    DATABASE_URL,
    # This argument is only needed for SQLite - remove when switching to Postgres
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependency — use this in your route functions to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()