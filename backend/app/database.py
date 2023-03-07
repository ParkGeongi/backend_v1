
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker, scoped_session
from app.env import DB_URL

engine = create_engine(DB_URL, echo=True, pool_pre_ping=True)
SessionLocal = scoped_session(
    sessionmaker(autocommit = False, autoflush=False, bind=engine)
)
Base = declarative_base()
engine = create_engine(DB_URL, echo=True, pool_pre_ping=True)
Base.query = SessionLocal.query_property()


async def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e