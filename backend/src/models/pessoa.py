import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import sqlite as _database
from . import endereco as _endereco
from sqlalchemy.ext.declarative import declared_attr

class Pessoa(_database.Base):
    __abstract__ = True
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    sobrenome = _sql.Column(_sql.String)
    cpf = _sql.Column(_sql.String)
    sexo = _sql.Column(_sql.String)
    raca = _sql.Column(_sql.String)

    @declared_attr
    def endereco_id(cls):
        return _sql.Column(_sql.Integer, _sql.ForeignKey(_endereco.Endereco.id))
    
    @declared_attr
    def endereco(cls):
        return _orm.relationship(_endereco.Endereco)