import sqlalchemy as _sql
from ..database import sqlite as _database


class Curso(_database.Base):
    __tablename__ = "curso"
    id_curso = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String, unique=True, index=True)
    campus = _sql.Column(_sql.String)
