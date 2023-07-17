import pydantic as _pydantic


class _DisciplinaBase(_pydantic.BaseModel):
    nome: str
    descricao: str
    id_curso: int

    class Config:
        orm_mode = True


class DisciplinaCreate(_DisciplinaBase):
    pass


class Disciplina(_DisciplinaBase):
    id_disciplina: int
