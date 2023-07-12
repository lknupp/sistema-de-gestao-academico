import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database


class Prerequisito(_database.Base):
    __tablename__ = 'prerequisito'
    id_prerequisito = _sql.Column(_sql.Integer, primary_key=True, index=True)

    id_disciplina = _sql.Column(
        _sql.Integer, _sql.ForeignKey('disciplina.id_disciplina'))
    disciplina = _orm.relationship(
        'Disciplina', back_populates='prerequisitos')
