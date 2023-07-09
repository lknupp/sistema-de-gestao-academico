import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List

from . import IRoute as _IRoute
from ..database import sqlite as _database
from ..schemas import professorSchema as _professorSchema
from ..controller import professorController as _controller

router = _fastapi.APIRouter()
controller = _controller.ProfessorController()


class ProfessorRoute(_IRoute.IRoute):
    @router.post("/api/professor/", response_model=_professorSchema.Professor)
    def criar(
        professor: _professorSchema.ProfessorCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        db_professor = controller.buscarPorCPF(db, cpf=professor.cpf)
        if db_professor:
            raise _fastapi.HTTPException(status_code=400, detail="CPF já cadastrado.")
        return controller.inserir(db, professor)

    @router.get("/api/professor/", response_model=List[_professorSchema.Professor])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        professors = controller.buscarTodos(db)
        if professors is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Professores não encontrados"
            )
        return professors

    @router.get(
        "/api/professor/{professor_id}", response_model=_professorSchema.Professor
    )
    def ler(professor_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        professor = controller.buscar(db, professor_id)
        if professor is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Professor não encontrado"
            )
        return professor
