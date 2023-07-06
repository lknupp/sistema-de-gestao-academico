import pydantic as _pydantic
import datetime as _dt


class _PessoaBase(_pydantic.BaseModel):
  nome: str
  sobrenome: str
  cpf: str
  sexo: str
  raca: str

  class Config:
    orm_mode = True


class PessoaCreate(_PessoaBase):
  pass


class Pessoa(_PessoaBase):
  id: int


class _AlunoBase(_PessoaBase):
  data_ingresso: _dt.date
  data_nascimento: _dt.date


class AlunoCreate(_AlunoBase):
  pass


class Aluno(_AlunoBase):
  id: int
