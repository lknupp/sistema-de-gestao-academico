import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus
from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import enderecoSchema as _enderecoSchema
from ..controller import enderecoController as _controller

router = _fastapi.APIRouter()
controller = _controller.EnderecoController()
tags_metadata = [
    {
        "name": "endereco",
        "description": "",
    }
]


class Route(_IRoute.IRoute):
    @router.post("/api/endereco/", response_model=_enderecoSchema.Endereco, status_code=HTTPStatus.CREATED.value, description=HTTPStatus.CREATED.phrase, tags=['endereco'])
    def criar(endereco: _enderecoSchema.EnderecoCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.inserir(db, endereco)

    @router.get("/api/endereco/", response_model=List[_enderecoSchema.Endereco], tags=['endereco'])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarTodos(db)

    @router.get("/api/endereco/{endereco_id}", response_model=_enderecoSchema.Endereco, tags=['endereco'])
    def ler(endereco_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscar(db, endereco_id)

    @router.put("/api/endereco/", response_model=_enderecoSchema.Endereco, tags=['endereco'])
    def atualizar(endereco: _enderecoSchema.Endereco, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, endereco)

    @router.delete("/api/endereco/", response_model=_enderecoSchema.Endereco, tags=['endereco'])
    def remover(endereco_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, endereco_id)
