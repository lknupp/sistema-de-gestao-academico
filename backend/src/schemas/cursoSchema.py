import pydantic as _pydantic


class _CursoBase(_pydantic.BaseModel):
    nome: str

    class Config:
        orm_mode = True


class CursoCreate(_CursoBase):
    pass


class Curso(_CursoBase):
    id_curso: int
