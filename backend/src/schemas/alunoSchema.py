import datetime as _dt

from . import pessoaSchema as _pessoa_schemas


class _AlunoBase(_pessoa_schemas._PessoaBase):
    data_ingresso: _dt.date
    data_nascimento: _dt.date


class AlunoCreate(_AlunoBase):
    pass


class Aluno(_AlunoBase):
    id_pessoa: int
