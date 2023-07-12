import sqlalchemy as _sql
from ...database import database as _database


class EnderecoBase(_database.Base):
    __abstract__ = True

    id_endereco = _sql.Column(_sql.Integer, primary_key=True, index=True)
    logradouro = _sql.Column(_sql.String)
    numero = _sql.Column(_sql.String)
    local = _sql.Column(_sql.String)
    cep = _sql.Column(_sql.String)
    tipo = _sql.Column(_sql.String)

    @classmethod
    def _get_table_name(cls):
        raise NotImplementedError("Subclasses devem implementar esse método.")
