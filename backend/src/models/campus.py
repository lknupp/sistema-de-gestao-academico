import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database
from .rl_campus_curso import rl_campus_curso


class Campus(_database.Base):
    __tablename__ = "campus"
    id_campus = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String, unique=True, index=True)
    id_endereco = _sql.Column(
        _sql.Integer, _sql.ForeignKey('endereco.id_endereco'))
    cursos = _orm.relationship(
        "Curso", secondary=rl_campus_curso, back_populates="campus"
    )
