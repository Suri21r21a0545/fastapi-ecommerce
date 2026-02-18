from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Change password to your MySQL password
DATABASE_URL = "mysql+pymysql://root:tiger@localhost/ecommerce_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
