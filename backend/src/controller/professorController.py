import sqlalchemy.orm as _orm
from typing import List

from .interface import IPessoaController as _pessoaController
from ..dao import professorDAO as _professorDAO
from ..schemas import professorSchema as _professorSchema
from ..models import professor as _professorModel


class ProfessorController(_pessoaController.IPessoaController):
    def __init__(self) -> None:
        super().__init__()
        self.professor_dao = _professorDAO.ProfessorDAO()

    def inserir(
        self, db: _orm.Session, pessoa: _professorSchema.ProfessorCreate
    ) -> _professorSchema.Professor:
        res = _professorModel.Professor(**pessoa.model_dump())
        return self.professor_dao.inserir(db, res)

    def atualizar(
        self, db: _orm.Session, pessoa: _professorSchema.Professor
    ) -> _professorSchema.Professor:
        res = _professorModel.Professor(**pessoa.model_dump())
        return self.professor_dao.atualizar(db, res)

    def remover(self, db: _orm.Session, id_pessoa: int) -> _professorSchema.Professor:
        res = self.professor_dao.remover(db, id_pessoa)
        return res

    def buscar(self, db: _orm.Session, id_pessoa: int) -> _professorSchema.Professor:
        res = self.professor_dao.buscar(db, id_pessoa)
        return res

    def buscarTodos(self, db: _orm.Session) -> List[_professorSchema.Professor]:
        res = self.professor_dao.buscarTodos(db)
        return res

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _professorSchema.Professor:
        res = self.professor_dao.buscarPorCPF(db, cpf)
        return res
