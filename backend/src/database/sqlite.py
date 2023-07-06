import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

SQLALCHEMY_DATABASE_URL = "sqlite:///./src/database/college.db"

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)
