import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database


class Disciplina(_database.Base):
    __tablename__ = "disciplina"

    __mapper_args__ = {"confirm_deleted_rows": False}

    id_disciplina = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    descricao = _sql.Column(_sql.String)

    prerequisitos = _orm.relationship(
        "Prerequisito", backref="disciplina", cascade="all, delete"
    )
    id_curso = _sql.Column(_sql.Integer, _sql.ForeignKey("curso.id_curso"))
