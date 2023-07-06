import sqlalchemy.orm as _orm

import backend.src.models.model as _model
import src.schemas as _schemas
from src.dao.pessoaDAO import AlunoDAO


class IPessoaController:
    def inserir(pessoa: _schemas.PessoaCreate) -> bool:
        pass

    def atualizar(pessoa: _schemas.PessoaCreate) -> bool:
        pass

    def remover(id: int) -> bool:
        pass

    def buscar(id: int) -> _schemas.Pessoa:
        pass

    def buscarPorCPF(cpf: str) -> _schemas.Pessoa:
        pass


class AlunoController(IPessoaController):
    def __init__(self) -> None:
        super().__init__()
        self.aluno_dao = AlunoDAO()

    def inserir(self, db: _orm.Session, aluno: _schemas.AlunoCreate) -> _schemas.Aluno:
        db_aluno = _model.Aluno(**aluno.dict())
        res = self.aluno_dao.inserir(db, aluno=db_aluno)
        return _schemas.Aluno.from_orm(res)

    def atualizar(self, db: _orm.Session, aluno: _schemas.AlunoCreate) -> bool:
        db_aluno = _model.Aluno(**aluno.dict())
        res = self.aluno_dao.atualizarDados(db, aluno=db_aluno)
        return _schemas.Aluno.from_orm(res)

    def remover(self, db: _orm.Session, body: dict) -> bool:
        res = self.aluno_dao.remover(db, body.id)
        return res

    def buscar(self, db: _orm.Session, body: dict) -> _schemas.Aluno:
        res = self.aluno_dao.buscar(db, body.id)
        return res

    def buscarTodos(self, db: _orm.Session) -> _schemas.Aluno:
        aluno_dao = AlunoDAO()
        res = self.aluno_dao.buscarTodos(db)
        return res

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _schemas.Aluno:
        res = self.aluno_dao.buscarPorCPF(db, cpf)
        return res
