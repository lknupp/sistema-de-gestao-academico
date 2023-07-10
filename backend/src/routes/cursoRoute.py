import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List

from .interface import IRoute as _IRoute
from ..database import sqlite as _database
from ..schemas import cursoSchema as _cursoSchema
from ..controller import cursoController as _controller

router = _fastapi.APIRouter()
controller = _controller.CursoController()


class CursoRoute(_IRoute.IRoute):
    @router.post("/api/curso/", response_model=_cursoSchema.Curso)
    def criar(
        curso: _cursoSchema.CursoCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        db_curso = controller.buscarCursoPorNome(db, curso_nome=curso.nome)
        if db_curso:
            raise _fastapi.HTTPException(
                status_code=400, detail="Curso já cadastrado.")
        return controller.inserir(db, curso)

    @router.get("/api/curso/", response_model=List[_cursoSchema.Curso])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        cursos = controller.buscarTodos(db)
        if cursos is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Não existem cursos cadastrados."
            )
        return cursos

    @router.get("/api/curso/curso-id/{curso_id}", response_model=_cursoSchema.Curso)
    def ler(curso_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        curso = controller.buscar(db, curso_id)
        if curso is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Curso não encontrado")
        return curso

    @router.get("/api/curso/curso-nome/{curso_nome}", response_model=_cursoSchema.Curso)
    def ler(curso_nome: str, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        curso = controller.buscarCursoPorNome(db, curso_nome)
        if curso is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Curso não encontrado")
        return curso

    @router.put("/api/curso/atualizar/", response_model=_cursoSchema.Curso)
    def atualizar(curso: _cursoSchema.Curso, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, curso)
