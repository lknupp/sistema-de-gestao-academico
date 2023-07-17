import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database


class Endereco(_database.Base):
    __tablename__ = "endereco"

    id_endereco = _sql.Column(_sql.Integer, primary_key=True, index=True)
    logradouro = _sql.Column(_sql.String)
    numero = _sql.Column(_sql.String)
    local = _sql.Column(_sql.String)
    cep = _sql.Column(_sql.String)
    tipo = _sql.Column(_sql.String)

    aluno = _orm.relationship("Aluno", backref="endereco", cascade="all, delete")
    professor = _orm.relationship(
        "Professor", backref="endereco", cascade="all, delete"
    )
