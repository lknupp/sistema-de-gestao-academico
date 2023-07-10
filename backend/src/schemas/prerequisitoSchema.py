import pydantic as _pydantic


class _PrerequisitoBase(_pydantic.BaseModel):
    id_disciplina: int

    class Config:
        orm_mode = True


class PrerequisitoCreate(_PrerequisitoBase):
    pass


class Prerequisito(_PrerequisitoBase):
    id_prerequisito: int
