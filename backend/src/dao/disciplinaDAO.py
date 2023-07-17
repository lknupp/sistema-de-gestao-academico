import sqlalchemy.orm as _orm
from typing import List

from ..models import disciplina as _disciplinaModel
from ..schemas import disciplinaSchema as _disciplinaSchema
from .interface import IDisciplinaDAO as _IDisciplinaDAO


class DisciplinaDAO(_IDisciplinaDAO.IDisciplinaDAO):
    def inserir(
        self, db: _orm.Session, disciplina: _disciplinaModel.Disciplina
    ) -> _disciplinaSchema.Disciplina:
        db.add(disciplina)
        db.commit()
        db.refresh(disciplina)
        return disciplina

    def atualizar(
        self, db: _orm.Session, disciplina: _disciplinaModel.Disciplina
    ) -> _disciplinaSchema.Disciplina:
        db.merge(disciplina)
        db.commit()
        db.refresh(disciplina)
        return disciplina

    def remover(
        self, db: _orm.Session, id_disciplina: int
    ) -> _disciplinaSchema.Disciplina:
        disciplina = (
            db.query(_disciplinaModel.Disciplina)
            .filter(_disciplinaModel.Disciplina.id_disciplina == id_disciplina)
            .first()
        )
        db.delete(disciplina)
        db.commit()
        return disciplina

    def buscar(
        self, db: _orm.Session, id_disciplina: int
    ) -> _disciplinaModel.Disciplina:
        disciplina = (
            db.query(_disciplinaModel.Disciplina)
            .filter(_disciplinaModel.Disciplina.id_disciplina == id_disciplina)
            .first()
        )
        return disciplina

    def buscarTodos(self, db: _orm.Session) -> List[_disciplinaModel.Disciplina]:
        disciplinas = db.query(_disciplinaModel.Disciplina).all()
        return disciplinas
