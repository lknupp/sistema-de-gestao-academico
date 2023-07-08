import sqlalchemy as _sql
from ..database import sqlite as _database

class Endereco(_database.Base):
    __tablename__ = 'endereco'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    logradouro = _sql.Column(_sql.String)
    numero = _sql.Column(_sql.String)
    local = _sql.Column(_sql.String)
    cep = _sql.Column(_sql.String)
    tipo = _sql.Column(_sql.String)
