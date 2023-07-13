import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database

class Telefone(_database.Base):
    __tablename__ = 'telefone'
    id_telefone = _sql.Column(_sql.Integer, primary_key=True, index=True)
    cod_pais = _sql.Column(_sql.Integer)
    ddd = _sql.Column(_sql.Integer)
    number = _sql.Column(_sql.Integer)

    aluno = _orm.relationship('Aluno', backref='telefone')
    professor = _orm.relationship('Professor', backref='telefone')

