import sqlalchemy as _sql
from ..database import database as _database
from sqlalchemy.ext.declarative import declared_attr


class Pessoa(_database.Base):
    __abstract__ = True
    id_pessoa = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String)
    sobrenome = _sql.Column(_sql.String)
    cpf = _sql.Column(_sql.String)
    sexo = _sql.Column(_sql.String)
    raca = _sql.Column(_sql.String)

    id_curso = _sql.Column(_sql.Integer, _sql.ForeignKey('curso.id_curso'))
    id_endereco = _sql.Column(_sql.Integer, _sql.ForeignKey('endereco.id_endereco'))
    id_telefone = _sql.Column(_sql.Integer, _sql.ForeignKey('telefone.id_telefone'))
