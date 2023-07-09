import sqlalchemy.orm as _orm
from typing import List

from .interface import IPessoaDAO as _IPessoaDAO
from ..models import aluno as _alunoModel
from ..schemas import alunoSchema as _alunoSchema


class AlunoDAO(_IPessoaDAO.IPessoaDAO):
    def inserir(
        self, db: _orm.Session, pessoa: _alunoModel.Aluno
    ) -> _alunoSchema.Aluno:
        db.add(pessoa)
        db.commit()
        db.refresh(pessoa)
        return pessoa

    def atualizar(
        self, db: _orm.Session, pessoa: _alunoModel.Aluno
    ) -> _alunoSchema.Aluno:
        db.query(_alunoModel.Aluno).filter(_alunoModel.Aluno.id == pessoa.id).update(
            pessoa
        )
        db.commit()
        db.refresh(pessoa)
        return pessoa

    def remover(self, db: _orm.Session, pessoa_id: int) -> _alunoSchema.Aluno:
        pessoa = (
            db.query(_alunoModel.Aluno)
            .filter(_alunoModel.Aluno.id == pessoa_id)
            .first()
        )
        db.remove(pessoa)
        db.commit()
        return pessoa

    def buscar(self, db: _orm.Session, pessoa_id: int) -> _alunoModel.Aluno:
        pessoa = (
            db.query(_alunoModel.Aluno)
            .filter(_alunoModel.Aluno.id == pessoa_id)
            .first()
        )
        return pessoa

    def buscarTodos(self, db: _orm.Session) -> List[_alunoModel.Aluno]:
        pessoas = db.query(_alunoModel.Aluno).all()
        return pessoas

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _alunoModel.Aluno:
        pessoa = (
            db.query(_alunoModel.Aluno).filter(_alunoModel.Aluno.cpf == cpf).first()
        )
        return pessoa

    def buscarAlunoPorAno(self, db: _orm.Session, ano: int) -> List[_alunoModel.Aluno]:
        pessoas = db.query(_alunoModel.Aluno).filter(_alunoModel.Aluno.ano == ano).all()
        return pessoas
