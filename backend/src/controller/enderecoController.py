import sqlalchemy.orm as _orm
from typing import List
import fastapi as _fastapi
from .interface import IEnderecoController as _enderecoController
from ..dao import enderecoDAO as _enderecoDAO
from ..schemas import enderecoSchema as _enderecoSchema
from ..models import endereco as _enderecoModel


class EnderecoController(_enderecoController.IEnderecoController):
    def __init__(self, model) -> None:
        super().__init__()
        if model == "aluno":
            self.endereco_dao = _enderecoDAO.EnderecoAlunoDAO()
            self.model = _enderecoModel.EnderecoAluno
        elif model == "professor":
            self.endereco_dao = _enderecoDAO.EnderecoProfessorDAO()
            self.model = _enderecoModel.EnderecoProfessor

    def inserir(
        self, db: _orm.Session, endereco: _enderecoSchema.EnderecoCreate
    ) -> _enderecoSchema.Endereco:
        endereco_db = self.model(**endereco.dict())
        return self.endereco_dao.inserir(db, endereco_db)

    def atualizar(
        self, db: _orm.Session, endereco: _enderecoSchema.Endereco
    ) -> _enderecoSchema.Endereco:
        endereco_db = self.endereco_dao.buscar(db, endereco.id_endereco)
        if not endereco_db:
            raise _fastapi.HTTPException(
                status_code=400, detail="Endereco não encontrado"
            )
        endereco_db = self.model(**endereco.dict())
        return self.endereco_dao.atualizar(db, endereco_db)

    def remover(
        self, db: _orm.Session, endereco_id: int
    ) -> _enderecoSchema.Endereco:
        try:
            res = self.endereco_dao.remover(db, endereco_id)
        except Exception as e:
            raise _fastapi.HTTPException(
                status_code=400, detail="{}".format(str(e))
            )
        return res

    def buscar(self, db: _orm.Session, endereco_id: int) -> _enderecoSchema.Endereco:
        return self.endereco_dao.buscar(db, endereco_id)

    def buscarTodos(self, db: _orm.Session) -> List[_enderecoSchema.Endereco]:
        return self.endereco_dao.buscarTodos(db)

    def buscarPorLogradouro(
        self, db: _orm.Session, logradouro: str
    ) -> List[_enderecoSchema.Endereco]:
        return self.endereco_dao.buscarPorLogradouro(db, logradouro)
