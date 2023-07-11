import sqlalchemy.orm as _orm
from typing import List

from .interface import IPessoaController as _pessoaController
from ..dao import alunoDAO as _alunoDAO
from ..schemas import alunoSchema as _alunoSchema
from ..models import aluno as _alunoModel


class AlunoController(_pessoaController.IPessoaController):
    def __init__(self) -> None:
        super().__init__()
        self.aluno_dao = _alunoDAO.AlunoDAO()

    def inserir(self, db: _orm.Session, pessoa: _alunoSchema.AlunoCreate) -> _alunoSchema.Aluno:
        res = _alunoModel.Aluno(**pessoa.dict())
        return self.aluno_dao.inserir(db, res)

    def atualizar(self, db: _orm.Session, pessoa: _alunoSchema.Aluno) -> _alunoSchema.Aluno:
        res = _alunoModel.Aluno(**pessoa.dict())
        return self.aluno_dao.atualizar(db, res)

    def remover(self, db: _orm.Session, id_pessoa: int) -> _alunoSchema.Aluno:
        res = self.aluno_dao.remover(db, id_pessoa)
        return res

    def buscar(self, db: _orm.Session, id_pessoa: int) -> _alunoSchema.Aluno:
        res = self.aluno_dao.buscar(db, id_pessoa)
        return res

    def buscarTodos(self, db: _orm.Session) -> List[_alunoSchema.Aluno]:
        res = self.aluno_dao.buscarTodos(db)
        return res

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _alunoSchema.Aluno:
        res = self.aluno_dao.buscarPorCPF(db, cpf)
        return res
