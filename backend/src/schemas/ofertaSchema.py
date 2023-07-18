import pydantic as _pydantic


class _OfertaBase(_pydantic.BaseModel):
    semestre: int
    ano: int
    id_professor: int
    id_disciplina: int
    periodo: str

    class Config:
        orm_mode = True


class OfertaCreate(_OfertaBase):
    pass


class Oferta(_OfertaBase):
    id_oferta: int
