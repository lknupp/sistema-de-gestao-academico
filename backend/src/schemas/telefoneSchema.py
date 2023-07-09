import pydantic as _pydantic


class _TelefoneBase(_pydantic.BaseModel):
    cod_pais: int
    ddd: int
    number: int
    id_pessoa: int

    class Config:
        orm_mode = True


class TelefoneCreate(_TelefoneBase):
    pass


class Telefone(_TelefoneBase):
    id_telefone: int
