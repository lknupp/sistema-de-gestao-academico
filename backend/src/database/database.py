import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os

DATABASE = os.getenv('DATABASE')
USER = os.getenv('APP_USER')
PASSWORD = os.getenv('APP_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URL = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)
