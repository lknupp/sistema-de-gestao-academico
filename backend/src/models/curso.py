import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import sqlite as _database


class Curso(_database.Base):
    __tablename__ = "curso"
    id_curso = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String, unique=True, index=True)
    campus = _sql.Column(_sql.String)

    disciplinas = _orm.relationship('Disciplina', back_populates='curso')
