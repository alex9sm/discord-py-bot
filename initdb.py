import logging
from sqlalchemy import (
    BigInteger,
    Boolean,
    Float,
    ForeignKey,
    create_engine,
    Column,
    String,
    Integer,
    UniqueConstraint,
    DateTime,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

#init database Main.db

import warnings
warnings.filterwarnings("ignore")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    discord_id = Column(BigInteger, unique=True, nullable=False)
    points = Column(Integer, default=0)

DATABASE_URL = "sqlite:///Main.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def init_db():
    Base.metadata.create_all(bind=engine)
    logging.debug("Database initialized")


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#end of init database 