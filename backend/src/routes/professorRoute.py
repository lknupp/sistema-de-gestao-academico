import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus
from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import professorSchema as _professorSchema
from ..controller import professorController as _controller

router = _fastapi.APIRouter()
controller = _controller.ProfessorController()


class ProfessorRoute(_IRoute.IRoute):
    @router.post("/api/professor/", response_model=_professorSchema.Professor, status_code=HTTPStatus.CREATED.value, description=HTTPStatus.CREATED.phrase)
    def criar(professor: _professorSchema.ProfessorCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        controller.buscarPorCPF(db, cpf=professor.cpf)
        return controller.inserir(db, professor)

    @router.get("/api/professor/", response_model=List[_professorSchema.Professor])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarTodos(db)

    @router.get("/api/professor/id/{id_professor}", response_model=_professorSchema.Professor)
    def ler(id_professor: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscar(db, id_professor)

    @router.get("/api/professor/cpf/{cpf}", response_model=_professorSchema.Professor)
    def ler_por_cpf(cpf: str, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarPorCPF(db, cpf)

    @router.put("/api/professor/", response_model=_professorSchema.Professor)
    def atualizar(professor: _professorSchema.Professor, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, professor)

    @router.delete("/api/professor/", response_model=_professorSchema.Professor)
    def remover(id_professor: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, id_professor)
