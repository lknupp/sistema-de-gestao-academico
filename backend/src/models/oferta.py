import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database

rl_historico = _sql.Table(
    "rl_historico",
    _database.Base.metadata,
    _sql.Column("id_historico", _sql.Integer, primary_key=True, index=True),
    _sql.Column("nota", _sql.Float),
    _sql.Column("faltas", _sql.Integer),
    _sql.Column("id_aluno_fk", _sql.Integer, _sql.ForeignKey("aluno.id_pessoa")),
    _sql.Column("id_oferta_fk", _sql.Integer, _sql.ForeignKey("oferta.id_oferta")),
)


class Oferta(_database.Base):
    __tablename__ = "oferta"
    id_oferta = _sql.Column(_sql.Integer, primary_key=True, index=True)
    ano = _sql.Column(_sql.Integer)
    semestre = _sql.Column(_sql.Integer)
    periodo = _sql.Column(_sql.String)

    historico = _orm.relationship(
        "Aluno", secondary=rl_historico, back_populates="ofertas"
    )
    id_disciplina = _sql.Column(
        _sql.Integer, _sql.ForeignKey("disciplina.id_disciplina")
    )
    id_professor = _sql.Column(_sql.Integer, _sql.ForeignKey("professor.id_pessoa"))
