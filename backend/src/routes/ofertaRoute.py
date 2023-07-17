import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus

from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import ofertaSchema as _ofertaSchema
from ..controller import ofertaController as _controller

router = _fastapi.APIRouter()
controller = _controller.OfertaController()
tags_metadata = [
    {
        "name": "oferta",
        "description": "",
    }
]


class OfertaRoute(_IRoute.IRoute):
    @router.post(
        "/api/oferta/",
        response_model=_ofertaSchema.Oferta,
        status_code=HTTPStatus.CREATED.value,
        description=HTTPStatus.CREATED.phrase,
        tags=["oferta"],
    )
    def criar(
        oferta: _ofertaSchema.OfertaCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        return controller.inserir(db, oferta)

    @router.get(
        "/api/oferta/",
        response_model=List[_ofertaSchema.Oferta],
        tags=["oferta"],
    )
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarTodos(db)

    @router.get(
        "/api/oferta/id/{id_oferta}",
        response_model=_ofertaSchema.Oferta,
        tags=["oferta"],
    )
    def ler(id_oferta: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscar(db, id_oferta)

    @router.put(
        "/api/oferta/",
        response_model=_ofertaSchema.Oferta,
        tags=["oferta"],
    )
    def atualizar(
        oferta: _ofertaSchema.Oferta,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        return controller.atualizar(db, oferta)

    @router.delete(
        "/api/oferta/",
        response_model=_ofertaSchema.Oferta,
        tags=["oferta"],
    )
    def remover(
        id_oferta: int, db: _orm.Session = _fastapi.Depends(_database.get_db)
    ):
        return controller.remover(db, id_oferta)
