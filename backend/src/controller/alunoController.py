import sqlalchemy.orm as _orm
from typing import List

from . import IPessoaController as _pessoaController
from ..dao import alunoDAO as _alunoDAO
from ..schemas import alunoSchema as _alunoSchema
from ..schemas import mensagemSchema as _msgSchema
from ..models import aluno as _alunoModel


class AlunoController(_pessoaController.IPessoaController):
    def __init__(self) -> None:
        super().__init__()
        self.aluno_dao = _alunoDAO.AlunoDAO()

    def inserir(
        self, db: _orm.Session, pessoa: _alunoSchema.AlunoCreate
    ) -> _msgSchema.Mensagem:
        db_aluno = _alunoModel.Aluno(**pessoa.dict())
        try:
            res = self.aluno_dao.inserir(db, db_aluno)
            return res
        except Exception as e:
            msg = _msgSchema.Mensagem(
                status=400,
                texto="Erro ao adicionar aluno.\n{}".format(e),
            )
            return msg

    def atualizar(
        self, db: _orm.Session, pessoa: _alunoSchema.AlunoCreate
    ) -> _msgSchema.Mensagem:
        db_aluno = _alunoModel.Aluno(**pessoa.dict())
        try:
            res = self.aluno_dao.atualizar(db, db_aluno)
            return res
        except Exception as e:
            msg = _msgSchema.Mensagem(
                status=400,
                texto="Erro ao atualizar aluno.\n{}".format(e),
            )
            return msg

    def remover(self, db: _orm.Session, pessoa_id: int) -> _msgSchema.Mensagem:
        try:
            res = self.aluno_dao.remover(db, pessoa_id)
            return res
        except Exception as e:
            msg = _msgSchema.Mensagem(
                status=400, texto="Erro ao remover aluno.\n{}".format(e)
            )
            return msg

    def buscar(self, db: _orm.Session, pessoa_id: int) -> _alunoSchema.Aluno:
        res = self.aluno_dao.buscar(db, pessoa_id)
        return res

    def buscarTodos(self, db: _orm.Session) -> List[_alunoSchema.Aluno]:
        res = self.aluno_dao.buscarTodos(db)
        return res

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _alunoSchema.Aluno:
        res = self.aluno_dao.buscarPorCPF(db, cpf)
        return res
