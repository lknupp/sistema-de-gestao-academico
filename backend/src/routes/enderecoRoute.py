import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List

from . import IRoute as _IRoute
from ..database import sqlite as _database
from ..schemas import enderecoSchema as _enderecoSchema
from ..schemas import mensagemSchema as _msgSchema
from ..controller import enderecoController as _controller

router = _fastapi.APIRouter()
controller = _controller.EnderecoController()


class AlunoRoute(_IRoute.IRoute):
    @router.post("/api/endereco/", response_model=_msgSchema.Mensagem)
    def criar(
        endereco: _enderecoSchema.EnderecoCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.inserir(db, endereco)

    @router.get("/api/endereco/", response_model=List[_enderecoSchema.Endereco])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        enderecos = controller.buscarTodos(db)
        if enderecos is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Endereços não encontrados"
            )
        return enderecos

    @router.get("/api/endereco/{endereco_id}", response_model=_enderecoSchema.Endereco)
    def ler(endereco_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        endereco = controller.buscar(db, endereco_id)
        if endereco is None:
            raise _fastapi.HTTPException(status_code=404, detail="Endereço não encontrado")
        return endereco
    
    @router.put("/api/endereco/", response_model=_msgSchema.Mensagem)
    def atualizar(
        endereco: _enderecoSchema.Endereco,
        db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, endereco)
    
    @router.delete("/api/endereco/", response_model=_msgSchema.Mensagem)
    def remover(
        endereco: _enderecoSchema.Endereco,
        db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, endereco)
    