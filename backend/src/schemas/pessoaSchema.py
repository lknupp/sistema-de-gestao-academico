import pydantic as _pydantic


class _PessoaBase(_pydantic.BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    sexo: str
    raca: str
    id_curso: int
    id_endereco: int
    id_telefone: int

    class Config:
        orm_mode = True


class PessoaCreate(_PessoaBase):
    pass


class Pessoa(_PessoaBase):
    id_pessoa: int
