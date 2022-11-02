from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://poridhi:iloveporidhi@localhost:5432/blog_service_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.schema = 'blog_service_fast'


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
