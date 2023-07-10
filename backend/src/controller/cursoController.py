import sqlalchemy.orm as _orm
from typing import List

from .interface import ICursoController as _ICursoController
from ..dao import cursoDAO as _cursoDAO
from ..schemas import cursoSchema as _cursoSchema
from ..models import curso as _cursoModel


class CursoController(_ICursoController.ICursoController):
    def __init__(self):
        super().__init__()
        self.curso_dao = _cursoDAO.CursoDAO()

    # TODO: Implementar Erros
    def inserir(self, db: _orm.Session, curso: _cursoSchema.CursoCreate):
        db_curso = _cursoModel.Curso(**curso.dict())
        print(db)
        try:
            curso = self.curso_dao.inserir(db=db, curso=db_curso)
        except Exception as e:
            pass
        return curso

    def atualizar(self, db: _orm.Session, curso: _cursoSchema.CursoCreate):
        db_curso = _cursoModel.Curso(**curso.dict())

        try:
            res = self.curso_dao.atualizar(db, db_curso)
            return res
        except Exception as e:
            pass

    def remover(self, db: _orm.Session, curso_id: int):
        try:
            res = self.curso_dao.remover(db, curso_id)
            return res
        except Exception as e:
            pass

    def buscar(self, db: _orm.Session, curso_id: int):
        return self.curso_dao.buscar(db, curso_id)

    def buscarTodos(self, db: _orm.Session):
        return self.curso_dao.buscarTodos(db)

    def buscarCursoPorNome(self, db: _orm.Session, curso_nome: str):
        return self.curso_dao.buscarCursoPorNome(db=db, curso_nome=curso_nome)
