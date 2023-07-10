import sqlalchemy.orm as _orm
from typing import List

from ..models import disciplina as _disciplinaModel
from ..schemas import disciplinaSchema as _disciplinaSchema
from .interface import disciplinaDAO as _IDisciplinaDAO

class DisciplinaDAO(_IDisciplinaDAO.IDisciplinaDAO):
    def inserir(
        self, db: _orm.Session, disciplina: _disciplinaModel.DisciplinaCreate
    ) -> _disciplinaSchema.Disciplina:
        db.add(disciplina)
        db.commit()
        db.refresh(disciplina)
        return disciplina

    def atualizar(
        self, db: _orm.Session, disciplina: _disciplinaModel.Disciplina
    ) -> _disciplinaSchema.Disciplina:
        db.query(_disciplinaModel.Disciplina).filter(_disciplinaModel.Disciplina.id == disciplina.id).update(
            disciplina
        )
        db.commit()
        db.refresh(disciplina)
        return disciplina

    def remover(self, db: _orm.Session, disciplina_id: int) -> _disciplinaSchema.Disciplina:
        disciplina = (
            db.query(_disciplinaModel.Disciplina)
            .filter(_disciplinaModel.Disciplina.id == disciplina_id)
            .first()
        )
        db.delete(disciplina)
        db.commit()
        return disciplina

    def buscar(self, db: _orm.Session, disciplina_id: int) -> _disciplinaModel.Disciplina:
        disciplina = (
            db.query(_disciplinaModel.Disciplina)
            .filter(_disciplinaModel.Disciplina.id == disciplina_id)
            .first()
        )
        return disciplina

