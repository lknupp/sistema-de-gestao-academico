import sqlalchemy as _sql

from ..database import database as _database
from . import pessoa as _pessoa


class Aluno(_pessoa.Pessoa, _database.Base):
    __tablename__ = "aluno"
    data_ingresso = _sql.Column(_sql.Date)
    data_nascimento = _sql.Column(_sql.Date)
