import pydantic as _pydantic


class _EnderecoBase(_pydantic.BaseModel):
    logradouro: str
    numero: str
    local: str
    cep: str
    tipo: str
    id_pessoa: int

    class Config:
        orm_mode = True


class EnderecoCreate(_EnderecoBase):
    pass


class Endereco(_EnderecoBase):
    id_endereco: int
