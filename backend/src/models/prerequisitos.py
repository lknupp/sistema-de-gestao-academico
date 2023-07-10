import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declared_attr
from ..database import sqlite as _database


class Prerequisito(_database.Base):
    __tablename__ = 'prerequisitos'
    id_prerequisito = _sql.Column(_sql.Integer, primary_key=True, index=True)
    
    @declared_attr
    def id_disciplina(cls):
        return _sql.Column(_sql.Integer, _sql.ForeignKey('disciplina.id_disciplina'))
