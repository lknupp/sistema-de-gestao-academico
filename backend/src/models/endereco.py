from .interface import IEndereco as _IEndereco


class EnderecoAluno(_IEndereco.EnderecoBase):
    __tablename__ = "endereco_aluno"

    @classmethod
    def _get_pessoa_table_name(cls):
        return "aluno"


class EnderecoProfessor(_IEndereco.EnderecoBase):
    __tablename__ = "endereco_professor"

    @classmethod
    def _get_pessoa_table_name(cls):
        return "professor"
