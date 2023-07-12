import pydantic as _pydantic


class _CampusBase(_pydantic.BaseModel):
    nome: str

    class Config:
        orm_mode = True


class CampusCreate(_CampusBase):
    pass


class Campus(_CampusBase):
    id_campus: int
