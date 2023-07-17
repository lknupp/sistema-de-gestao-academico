import sqlalchemy as _sql

from ..database import database as _database
from . import pessoa as _pessoa
from . import oferta as _oferta

class Aluno(_pessoa.Pessoa, _database.Base):
    __tablename__ = "aluno"
    data_ingresso = _sql.Column(_sql.Date)
    data_nascimento = _sql.Column(_sql.Date)

    ofertas = _sql.orm.relationship("Oferta", secondary=_oferta.rl_historico, back_populates="historico")
