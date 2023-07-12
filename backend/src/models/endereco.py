from .interface import IEndereco as _IEndereco
import sqlalchemy as _sql


class EnderecoAluno(_IEndereco.EnderecoBase):
    __tablename__ = "endereco_aluno"
    id_pessoa = _sql.Column(_sql.Integer, _sql.ForeignKey('aluno.id_pessoa'))

    @classmethod
    def _get_table_name(cls):
        return "aluno"


class EnderecoProfessor(_IEndereco.EnderecoBase):
    __tablename__ = "endereco_professor"
    id_pessoa = _sql.Column(
        _sql.Integer, _sql.ForeignKey('professor.id_pessoa'))

    @classmethod
    def _get_table_name(cls):
        return "professor"


class EnderecoCampus(_IEndereco.EnderecoBase):
    __tablename__ = "endereco_campus"
    id_campus = _sql.Column(_sql.Integer, _sql.ForeignKey('campus.id_campus'))

    @classmethod
    def _get_table_name(cls):
        return "campus"
