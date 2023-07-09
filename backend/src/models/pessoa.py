import sqlalchemy as _sql
from ..database import sqlite as _database
import sqlalchemy.orm as _orm
from sqlalchemy.ext.declarative import declared_attr
from . import endereco as _endereco


class Pessoa(_database.Base):
    __abstract__ = True
    id_pessoa = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    sobrenome = _sql.Column(_sql.String)
    cpf = _sql.Column(_sql.String)
    sexo = _sql.Column(_sql.String)
    raca = _sql.Column(_sql.String)
