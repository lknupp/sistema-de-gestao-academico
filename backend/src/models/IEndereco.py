import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declared_attr
from ..database import sqlite as _database


class EnderecoBase(_database.Base):
    __abstract__ = True

    id_endereco = _sql.Column(_sql.Integer, primary_key=True, index=True)
    logradouro = _sql.Column(_sql.String)
    numero = _sql.Column(_sql.String)
    local = _sql.Column(_sql.String)
    cep = _sql.Column(_sql.String)
    tipo = _sql.Column(_sql.String)

    @declared_attr
    def id_pessoa(cls):
        return _sql.Column(_sql.Integer, _sql.ForeignKey(cls._get_pessoa_table_name()))

    @classmethod
    def _get_pessoa_table_name(cls):
        raise NotImplementedError("Subclasses devem implementar esse método.")
