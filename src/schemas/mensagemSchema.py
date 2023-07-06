import pydantic as _pydantic


class _MensagemBase(_pydantic.BaseModel):
    id: int
    texto: str


class Mensagem(_MensagemBase):
    pass
