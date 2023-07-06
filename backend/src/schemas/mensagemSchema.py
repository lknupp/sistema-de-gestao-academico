import pydantic as _pydantic


class _MensagemBase(_pydantic.BaseModel):
    success: bool
    status: int
    texto: str


class Mensagem(_MensagemBase):
    pass
