import sqlalchemy as _sql
from ..database import database as _database


class Prerequisito(_database.Base):
    __tablename__ = "prerequisito"
    id_prerequisito = _sql.Column(_sql.Integer, primary_key=True, index=True)
    disciplina_prerequisito = _sql.Column(_sql.Integer)

    id_disciplina = _sql.Column(
        _sql.Integer, _sql.ForeignKey("disciplina.id_disciplina", ondelete="CASCADE")
    )
