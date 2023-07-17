import sqlalchemy.orm as _orm
from typing import List

from .interface import IDisciplinaController as _disciplinaController
from ..dao import disciplinaDAO as _disciplinaDAO
from ..schemas import disciplinaSchema as _disciplinaSchema
from ..models import disciplina as _disciplinaModel


class DisciplinaController(_disciplinaController.IDisciplinaController):
    def __init__(self) -> None:
        super().__init__()
        self.disciplina_dao = _disciplinaDAO.DisciplinaDAO()

    def inserir(
        self, db: _orm.Session, disciplina: _disciplinaSchema.DisciplinaCreate
    ) -> _disciplinaSchema.Disciplina:
        res = _disciplinaModel.Disciplina(**disciplina.model_dump())
        return self.disciplina_dao.inserir(db, res)

    def atualizar(
        self, db: _orm.Session, disciplina: _disciplinaSchema.Disciplina
    ) -> _disciplinaSchema.Disciplina:
        res = _disciplinaModel.Disciplina(**disciplina.model_dump())
        return self.disciplina_dao.atualizar(db, res)

    def remover(
        self, db: _orm.Session, id_disciplina: int
    ) -> _disciplinaSchema.Disciplina:
        res = self.disciplina_dao.remover(db, id_disciplina)
        return res

    def buscar(
        self, db: _orm.Session, id_disciplina: int
    ) -> _disciplinaSchema.Disciplina:
        res = self.disciplina_dao.buscar(db, id_disciplina)
        return res

    def buscarTodos(self, db: _orm.Session) -> List[_disciplinaSchema.Disciplina]:
        res = self.disciplina_dao.buscarTodos(db)
        return res
