import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declared_attr
from ..database import sqlite as _database


class TelefoneBase(_database.Base):
    __abstract__ = True

    id_telefone = _sql.Column(_sql.Integer, primary_key=True, index=True)
    cod_pais = _sql.Column(_sql.Integer)
    ddd = _sql.Column(_sql.Integer)
    number = _sql.Column(_sql.Integer)

    @declared_attr
    def id_pessoa(cls):
        return _sql.Column(_sql.Integer, _sql.ForeignKey(cls._get_pessoa_table_name()))

    @classmethod
    def _get_pessoa_table_name(cls):
        raise NotImplementedError("Subclasses devem implementar esse método.")
