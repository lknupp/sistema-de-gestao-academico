import datetime as _dt

from . import pessoaSchema as _pessoa_schemas


class _ProfessorBase(_pessoa_schemas._PessoaBase):
    dataContratacao: _dt.date
    departamento: str
    salario: float


class ProfessorCreate(_ProfessorBase):
    pass


class Professor(_ProfessorBase):
    id_pessoa: int
