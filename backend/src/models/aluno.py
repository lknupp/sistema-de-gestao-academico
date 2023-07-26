import sqlalchemy as _sql
import sqlalchemy.orm as _orm

from ..database import database as _database
from . import pessoa as _pessoa


rl_historico = _sql.Table(
    "rl_historico",
    _database.Base.metadata,
    _sql.Column("id_historico", _sql.Integer, primary_key=True, index=True),
    _sql.Column("nota", _sql.Float),
    _sql.Column("faltas", _sql.Integer),
    _sql.Column("id_aluno_fk", _sql.Integer, _sql.ForeignKey("aluno.id_pessoa")),
    _sql.Column("id_oferta_fk", _sql.Integer, _sql.ForeignKey("oferta.id_oferta")),
)


class Aluno(_pessoa.Pessoa, _database.Base):
    __tablename__ = "aluno"
    data_ingresso = _sql.Column(_sql.Date)
    data_nascimento = _sql.Column(_sql.Date)

    historico = _orm.relationship(
        "Oferta", secondary=rl_historico, back_populates="ofertas"
    )
