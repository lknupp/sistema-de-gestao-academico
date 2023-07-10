import sqlalchemy as _sql
from ..database import sqlite as _database
from sqlalchemy.ext.declarative import declared_attr


class Pessoa(_database.Base):
    __abstract__ = True
    id_pessoa = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    sobrenome = _sql.Column(_sql.String)
    cpf = _sql.Column(_sql.String)
    sexo = _sql.Column(_sql.String)
    raca = _sql.Column(_sql.String)

    @declared_attr
    def id_curso(cls):
        return _sql.Column(_sql.Integer, _sql.ForeignKey('curso.id_curso'))
