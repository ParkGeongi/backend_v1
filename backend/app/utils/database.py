from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.utils.env import DB_URL, DB_HOST, PORT, DB_USER, DB_PASSWORD, DB_NAME, CHARSET
import pymysql
from typing import Generator

Base = declarative_base()
engine = create_engine(DB_URL, echo=True)
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=DB_HOST, port=PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset=CHARSET)
SessionLocal = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False)
)
Base.query = SessionLocal.query_property()


async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
