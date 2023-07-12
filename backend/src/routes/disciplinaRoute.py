import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus

from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import disciplinaSchema as _disciplinaSchema
from ..controller import disciplinaController as _controller
from ..controller import prerequisitoController as _prerequisitoController

router = _fastapi.APIRouter()
controller = _controller.DisciplinaController()
pr_controller = _prerequisitoController.PrerequisitoController()


class DisciplinaRoute(_IRoute.IRoute):
    @router.post("/api/disciplina/", response_model=_disciplinaSchema.Disciplina, status_code=HTTPStatus.CREATED.value, description=HTTPStatus.CREATED.phrase)
    def criar(disciplina: _disciplinaSchema.DisciplinaCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.inserir(db, disciplina)

    @router.get("/api/disciplina/", response_model=List[_disciplinaSchema.Disciplina])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarTodos(db)

    @router.get("/api/disciplina/id/{id_disciplina}", response_model=_disciplinaSchema.Disciplina)
    def ler(id_disciplina: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscar(db, id_disciplina)

    @router.put("/api/disciplina/", response_model=_disciplinaSchema.Disciplina)
    def atualizar(disciplina: _disciplinaSchema.Disciplina, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, disciplina)

    @router.delete("/api/disciplina/", response_model=_disciplinaSchema.Disciplina)
    def remover(id_disciplina: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, id_disciplina)
