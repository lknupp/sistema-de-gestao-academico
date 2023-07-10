import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import sqlite as _database


class Disciplina(_database.Base):
    __tablename__ = 'disciplina'
    id_disciplina = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    descricao = _sql.Column(_sql.String)

    id_curso = _sql.Column(_sql.Integer, _sql.ForeignKey('curso.id_curso'))
    curso = _orm.relationship('Curso', back_populates='disciplinas')

    prerequisitos = _orm.relationship('Prerequisito', back_populates='disciplina')
