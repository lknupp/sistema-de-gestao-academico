import pydantic as _pydantic


class _MensagemBase(_pydantic.BaseModel):
    status: int
    texto: str

    class Config:
        orm_mode = True


class Mensagem(_MensagemBase):
    pass
