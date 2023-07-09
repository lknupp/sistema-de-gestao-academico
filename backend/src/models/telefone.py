from . import ITelefone as _ITelefone


class TelefoneAluno(_ITelefone.TelefoneBase):
    __tablename__ = "telefone_aluno"

    @classmethod
    def _get_pessoa_table_name(cls):
        return "aluno"


class TelefoneProfessor(_ITelefone.TelefoneBase):
    __tablename__ = "telefone_professor"

    @classmethod
    def _get_pessoa_table_name(cls):
        return "professor"
