# backend/config/dependencies.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session as SQLAlchemySession

# Configure the database engine and session factory
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> SQLAlchemySession:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
