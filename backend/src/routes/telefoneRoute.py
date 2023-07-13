import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus
from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import telefoneSchema as _telefoneSchema
from ..controller import telefoneController as _controller

router = _fastapi.APIRouter()
controller = _controller.TelefoneController()


class TelefoneRoute(_IRoute.IRoute):
    @router.post("/api/telefone/", response_model=_telefoneSchema.Telefone, status_code=HTTPStatus.CREATED.value, description=HTTPStatus.CREATED.phrase)
    def criar(telefone: _telefoneSchema.TelefoneCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.inserir(db, telefone)

    @router.get("/api/telefone/", response_model=List[_telefoneSchema.Telefone])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarTodos(db)

    @router.get("/api/telefone/{telefone_id}", response_model=_telefoneSchema.Telefone)
    def ler(telefone_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscar(db, telefone_id)

    @router.put("/api/telefone/", response_model=_telefoneSchema.Telefone)
    def atualizar(telefone: _telefoneSchema.Telefone, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, telefone)

    @router.delete("/api/telefone/", response_model=_telefoneSchema.Telefone)
    def remover(telefone_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, telefone_id)
