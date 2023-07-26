import sqlalchemy as _sql

from ..database import database as _database
from . import pessoa as _pessoa


class Professor(_pessoa.Pessoa, _database.Base):
    __tablename__ = "professor"
    data_contratacao = _sql.Column(_sql.Date)
    departamento = _sql.Column(_sql.String)
    salario = _sql.Column(_sql.Float)
