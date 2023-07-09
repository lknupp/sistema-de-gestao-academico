import sqlalchemy.orm as _orm
from typing import List
from ..models import curso as _cursoModel
from .interface import ICursoDAO as _ICursoDAO


class CursoDAO(_ICursoDAO.ICursoDAO):
    def inserir(self, db: _orm.Session, curso: _cursoModel.Curso):
        db.add(curso)
        db.commit()
        db.refresh(curso)

        return curso

    def atualizar(self, db: _orm.Session, curso: _cursoModel.Curso):
        db.query(_cursoModel.Curso).filter(_cursoModel.Curso.id == curso.id).update(
            curso
        )
        db.commit()
        db.refresh(curso)

        return curso

    def remover(self, db: _orm.Session, curso_id: int):
        db.remove(
            db.query(_cursoModel.Curso).filter(_cursoModel.Curso.id == curso_id).first()
        )
        db.commit()
        db.refresh()

    def buscarTodos(self, db: _orm.Session) -> List[_cursoModel.Curso]:
        return db.query(_cursoModel.Curso).all()

    def buscarCursoPorNome(self, db: _orm.Session, curso_nome: str):
        return (
            db.query(_cursoModel.Curso)
            .filter(_cursoModel.Curso.nome == curso_nome)
            .first()
        )
