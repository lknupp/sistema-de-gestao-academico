import sqlalchemy.orm as _orm
from typing import List

from . import IPessoaDAO as _IPessoaDAO
from ..models import aluno as _alunoModel
from ..schemas import mensagemSchema as _msgSchema


class AlunoDAO(_IPessoaDAO.IPessoaDAO):
    def inserir(
        self, db: _orm.Session, pessoa: _alunoModel.Aluno
    ) -> _msgSchema.Mensagem:
        db.add(pessoa)
        db.commit()
        mensagem = _msgSchema.Mensagem(
            status=200, texto="Aluno cadastrado com sucesso."
        )
        return mensagem

    def atualizar(
        self, db: _orm.Session, pessoa: _alunoModel.Aluno
    ) -> _msgSchema.Mensagem:
        db.query(_alunoModel.Aluno).filter(_alunoModel.Aluno.id == pessoa.id).update(
            pessoa
        )
        db.commit()
        mensagem = _msgSchema.Mensagem(
            status=200, texto="Aluno atualizado com sucesso."
        )
        return mensagem

    def remover(self, db: _orm.Session, pessoa_id: int) -> _msgSchema.Mensagem:
        db.remove(
            db.query(_alunoModel.Aluno)
            .filter(_alunoModel.Aluno.id == pessoa_id)
            .first()
        )
        db.commit()
        mensagem = _msgSchema.Mensagem(status=200, texto="Aluno removido com sucesso.")
        return mensagem

    def buscar(self, db: _orm.Session, pessoa_id: int) -> _alunoModel.Aluno:
        aluno = (
            db.query(_alunoModel.Aluno)
            .filter(_alunoModel.Aluno.id == pessoa_id)
            .first()
        )
        return aluno

    def buscarTodos(self, db: _orm.Session) -> List[_alunoModel.Aluno]:
        alunos = db.query(_alunoModel.Aluno).all()
        return alunos

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _alunoModel.Aluno:
        aluno = db.query(_alunoModel.Aluno).filter(_alunoModel.Aluno.cpf == cpf).first()
        return aluno

    def filtrarPorAno(self, db: _orm.Session, ano: int) -> List[_alunoModel.Aluno]:
        alunos = db.query(_alunoModel.Aluno).filter(_alunoModel.Aluno.ano == ano).all()
        return alunos
