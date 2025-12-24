from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# CHANGE ONLY THE PASSWORD BELOW
DATABASE_URL = "postgresql+psycopg2://postgres:Sri@localhost:5432/authdb"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

