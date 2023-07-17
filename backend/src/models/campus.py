import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database

rl_campus_curso = _sql.Table(
    "rl_campus_curso",
    _database.Base.metadata,
    _sql.Column("id", _sql.Integer, primary_key=True, index=True),
    _sql.Column("id_curso_fk", _sql.Integer, _sql.ForeignKey("curso.id_curso")),
    _sql.Column("id_campus_fk", _sql.Integer, _sql.ForeignKey("campus.id_campus")),
)


class Campus(_database.Base):
    __tablename__ = "campus"
    id_campus = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String, unique=True, index=True)
    cursos = _orm.relationship(
        "Curso", secondary=rl_campus_curso, back_populates="campus"
    )
