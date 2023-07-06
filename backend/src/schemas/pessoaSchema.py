import pydantic as _pydantic


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
