import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus
from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import prerequisitoSchema as _prerequisitoSchema
from ..controller import prerequisitoController as _controller

router = _fastapi.APIRouter()
controller = _controller.PrerequisitoController()
tags_metadata = [
    {
        "name": "pre-requisito",
        "description": "",
    }
]


class PrerequisitoRoute(_IRoute.IRoute):
    @router.post("/api/prerequisito/", response_model=_prerequisitoSchema.Prerequisito, status_code=HTTPStatus.CREATED.value, description=HTTPStatus.CREATED.phrase, tags=['pre-requisito'])
    def criar(prerequisito: _prerequisitoSchema.PrerequisitoCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.inserir(db, prerequisito)

    @router.get("/api/prerequisito/id/{id_prerequisito}", response_model=_prerequisitoSchema.Prerequisito, tags=['pre-requisito'])
    def ler(id_prerequisito: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscar(db, id_prerequisito)

    @router.put("/api/prerequisito/", response_model=_prerequisitoSchema.Prerequisito, tags=['pre-requisito'])
    def atualizar(prerequisito: _prerequisitoSchema.Prerequisito, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, prerequisito)

    @router.delete("/api/prerequisito/", response_model=_prerequisitoSchema.Prerequisito, tags=['pre-requisito'])
    def remover(id_prerequisito: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, id_prerequisito)
