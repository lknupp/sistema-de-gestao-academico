import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declared_attr
from ..database import sqlite as _database


class TelefoneAluno(_database.Base):
    __tablename__ = 'telefone_aluno'
    id_telefone = _sql.Column(_sql.Integer, primary_key=True, index=True)
    cod_pais = _sql.Column(_sql.Integer)
    ddd = _sql.Column(_sql.Integer)
    numero = _sql.Column(_sql.String)

    @declared_attr
    def id_pessoa(self):
        return _sql.Column(_sql.Integer, _sql.ForeignKey('aluno.id_pessoa'))
    
class EnderecoProfessor(_database.Base):
    __tablename__ = 'endereco_professor'
    id_endereco = _sql.Column(_sql.Integer, primary_key=True, index=True)
    logradouro = _sql.Column(_sql.String)
    numero = _sql.Column(_sql.String)
    local = _sql.Column(_sql.String)
    cep = _sql.Column(_sql.String)
    tipo = _sql.Column(_sql.String)

    @declared_attr
    def id_pessoa(self):
        return _sql.Column(_sql.Integer, _sql.ForeignKey('professor.id_pessoa'))

