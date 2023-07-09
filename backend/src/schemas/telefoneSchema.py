import pydantic as _pydantic


class _TelefoneBase(_pydantic.BaseModel):
    cod_pais: int
    ddd: int
    numero: int
    id_pessoa: int

    class Config:
        orm_mode = True


class EnderecoCreate(_TelefoneBase):
    pass


class Endereco(_TelefoneBase):
    id_telefone: int
