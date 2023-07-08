import pydantic as _pydantic


class _EnderecoBase(_pydantic.BaseModel):
    logradouro: str
    numero: str
    local: str
    cep: str
    tipo: str

    class Config:
        orm_mode = True


class EnderecoCreate(_EnderecoBase):
    pass


class Endereco(_EnderecoBase):
    id: int
