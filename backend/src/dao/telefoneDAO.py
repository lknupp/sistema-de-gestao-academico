import sqlalchemy.orm as _orm
from typing import List

from .interface import ITelefoneDAO as _ITelefoneDAO
from ..models import telefone as _telefoneModel
from ..schemas import telefoneSchema as _telefoneSchema


class TelefoneAlunoDAO(_ITelefoneDAO.ITelefoneDAO):
    def inserir(
        self, db: _orm.Session, telefone: _telefoneModel.TelefoneAluno
    ) -> _telefoneSchema.Telefone:
        db.add(telefone)
        db.commit()
        db.refresh(telefone)
        return telefone

    def atualizar(
        self, db: _orm.Session, telefone: _telefoneModel.TelefoneAluno
    ) -> _telefoneModel.TelefoneAluno:
        db.query(_telefoneModel.TelefoneAluno).filter(
            _telefoneModel.TelefoneAluno.id == telefone.id
        ).update(telefone)
        db.commit()
        db.refresh(telefone)
        return telefone

    def remover(
        self, db: _orm.Session, telefone_id: int
    ) -> _telefoneModel.TelefoneAluno:
        telefone = (
            db.query(_telefoneModel.TelefoneAluno)
            .filter(_telefoneModel.TelefoneAluno.id == telefone_id)
            .first()
        )
        db.remove(telefone)
        db.commit()
        return telefone

    def buscar(
        self, db: _orm.Session, telefone_id: int
    ) -> _telefoneModel.TelefoneAluno:
        telefone = (
            db.query(_telefoneModel.TelefoneAluno)
            .filter(_telefoneModel.TelefoneAluno.id == telefone_id)
            .first()
        )
        return telefone

    def buscarTodos(self, db: _orm.Session) -> List[_telefoneModel.TelefoneAluno]:
        telefones = db.query(_telefoneModel.TelefoneAluno).all()
        return telefones

    def buscarPorDdd(self, db: _orm.Session, ddd: int) -> _telefoneModel.TelefoneAluno:
        telefone = (
            db.query(_telefoneModel.TelefoneAluno)
            .filter(_telefoneModel.TelefoneAluno.ddd == ddd)
            .first()
        )
        return telefone


class TelefoneProfessorDAO(_ITelefoneDAO.ITelefoneDAO):
    def inserir(
        self, db: _orm.Session, telefone: _telefoneModel.TelefoneProfessor
    ) -> _telefoneSchema.Telefone:
        db.add(telefone)
        db.commit()
        db.refresh(telefone)
        return telefone

    def atualizar(
        self, db: _orm.Session, telefone: _telefoneModel.TelefoneProfessor
    ) -> _telefoneModel.TelefoneProfessor:
        db.query(_telefoneModel.TelefoneProfessor).filter(
            _telefoneModel.TelefoneProfessor.id == telefone.id
        ).update(telefone)
        db.commit()
        db.refresh(telefone)
        return telefone

    def remover(
        self, db: _orm.Session, telefone_id: int
    ) -> _telefoneModel.TelefoneProfessor:
        telefone = (
            db.query(_telefoneModel.TelefoneProfessor)
            .filter(_telefoneModel.TelefoneProfessor.id == telefone_id)
            .first()
        )
        db.remove(telefone)
        db.commit()
        return telefone

    def buscar(
        self, db: _orm.Session, telefone_id: int
    ) -> _telefoneModel.TelefoneProfessor:
        telefone = (
            db.query(_telefoneModel.TelefoneProfessor)
            .filter(_telefoneModel.TelefoneProfessor.id == telefone_id)
            .first()
        )
        return telefone

    def buscarTodos(self, db: _orm.Session) -> List[_telefoneModel.TelefoneProfessor]:
        telefones = db.query(_telefoneModel.TelefoneProfessor).all()
        return telefones

    def buscarPorDdd(
        self, db: _orm.Session, ddd: int
    ) -> _telefoneModel.TelefoneProfessor:
        telefone = (
            db.query(_telefoneModel.TelefoneProfessor)
            .filter(_telefoneModel.TelefoneProfessor.ddd == ddd)
            .first()
        )
        return telefone
