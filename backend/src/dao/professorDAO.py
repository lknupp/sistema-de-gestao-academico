import sqlalchemy.orm as _orm
from typing import List

from . import IPessoaDAO as _IPessoaDAO
from ..models import professor as _professorModel
from ..schemas import professorSchema as _professorSchema


class ProfessorDAO(_IPessoaDAO.IPessoaDAO):
    def inserir(
        self, db: _orm.Session, pessoa: _professorModel.Professor
    ) -> _professorSchema.Professor:
        db.add(pessoa)
        db.commit()
        db.refresh(pessoa)
        return pessoa

    def atualizar(
        self, db: _orm.Session, pessoa: _professorModel.Professor
    ) -> _professorSchema.Professor:
        db.query(_professorModel.Professor).filter(_professorModel.Professor.id == pessoa.id).update(pessoa)
        db.commit()
        db.refresh(pessoa)
        return pessoa

    def remover(self, db: _orm.Session, pessoa_id: int) -> _professorSchema.Professor:
        pessoa = db.query(_professorModel.Professor).filter(_professorModel.Professor.id == pessoa_id).first()
        db.remove(pessoa)
        db.commit()
        return pessoa

    def buscar(self, db: _orm.Session, pessoa_id: int) -> _professorModel.Professor:
        pessoa = (
            db.query(_professorModel.Professor)
            .filter(_professorModel.Professor.id == pessoa_id)
            .first())
        return pessoa

    def buscarTodos(self, db: _orm.Session) -> List[_professorModel.Professor]:
        pessoas = db.query(_professorModel.Professor).all()
        return pessoas

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _professorModel.Professor:
        pessoa = db.query(_professorModel.Professor).filter(_professorModel.Professor.cpf == cpf).first()
        return pessoa

    def buscarProfessorPorAno(self, db: _orm.Session, ano: int) -> List[_professorModel.Professor]:
        pessoas = db.query(_professorModel.Professor).filter(_professorModel.Professor.ano == ano).all()
        return pessoas
