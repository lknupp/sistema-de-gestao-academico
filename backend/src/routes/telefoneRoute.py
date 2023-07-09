import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List

from . import IRoute as _IRoute
from ..database import sqlite as _database
from ..schemas import telefoneSchema as _telefoneSchema
from ..controller import telefoneController as _controller

router = _fastapi.APIRouter()
controller = _controller.TelefoneController("aluno")


class AlunoRoute(_IRoute.IRoute):
    @router.post("/api/telefone/", response_model=_telefoneSchema.Telefone)
    def criar(
        telefone: _telefoneSchema.TelefoneCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        return controller.inserir(db, telefone)

    @router.get("/api/telefone/", response_model=List[_telefoneSchema.Telefone])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        telefones = controller.buscarTodos(db)
        if telefones is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Telefones não encontrados"
            )
        return telefones

    @router.get("/api/telefone/{telefone_id}", response_model=_telefoneSchema.Telefone)
    def ler(telefone_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        telefone = controller.buscar(db, telefone_id)
        if telefone is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Telefone não encontrado"
            )
        return telefone

    @router.put("/api/telefone/", response_model=_telefoneSchema.Telefone)
    def atualizar(
        telefone: _telefoneSchema.Telefone,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        return controller.atualizar(db, telefone)

    @router.delete("/api/telefone/", response_model=_telefoneSchema.Telefone)
    def remover(
        telefone: _telefoneSchema.Telefone,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        return controller.remover(db, telefone)
