import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


load_dotenv()

# Load database URL from environment. Provide a sensible default for local development
# but avoid committing real credentials. Update your .env file or environment
# before running the application.
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://user:password@localhost:5432/dbname'  # placeholder default
)

engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL logs
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()