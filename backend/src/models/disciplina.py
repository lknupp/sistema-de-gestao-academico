import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from sqlalchemy.ext.declarative import declared_attr
from ..database import sqlite as _database


class Disciplina(_database.Base):
    __tablename__ = 'disciplina'
    id_disciplina = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    descricao = _sql.Column(_sql.String)

    @declared_attr
    def id_curso(cls):
        return _sql.Column(_sql.Integer, _sql.ForeignKey('curso.id_curso'))
    
    prerequisitos = _orm.relationship('Prerequisito', backref='disciplina')

