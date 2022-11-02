from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

db_config = config.DBSettings()
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{db_config.DB_USER}:{db_config.DB_PASSWORD}@{db_config.DB_HOST}:{db_config.DB_PORT}/{db_config.DB_NAME}"
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
