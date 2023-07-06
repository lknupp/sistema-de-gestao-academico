import sqlalchemy as _sql

from ..database import sqlite as _database


class Pessoa(_database.Base):
    __abstract__ = True
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    sobrenome = _sql.Column(_sql.String)
    cpf = _sql.Column(_sql.String)
    sexo = _sql.Column(_sql.String)
    raca = _sql.Column(_sql.String)
