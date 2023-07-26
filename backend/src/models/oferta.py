import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database
from . import aluno as _aluno



class Oferta(_database.Base):
    __tablename__ = "oferta"
    id_oferta = _sql.Column(_sql.Integer, primary_key=True, index=True)
    ano = _sql.Column(_sql.Integer)
    semestre = _sql.Column(_sql.Integer)
    periodo = _sql.Column(_sql.String)

    ofertas = _sql.orm.relationship(
        "Aluno", secondary=_aluno.rl_historico, back_populates="historico"
    )

    id_disciplina = _sql.Column(
        _sql.Integer, _sql.ForeignKey("disciplina.id_disciplina")
    )
    id_professor = _sql.Column(_sql.Integer, _sql.ForeignKey("professor.id_pessoa"))
