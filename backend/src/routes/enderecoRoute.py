import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List

from .interface import IRoute as _IRoute
from ..database import sqlite as _database
from ..schemas import enderecoSchema as _enderecoSchema
from ..controller import enderecoController as _controller

router = _fastapi.APIRouter()
controllerAluno = _controller.EnderecoController("aluno")
controllerProfessor = _controller.EnderecoController("professor")

class AlunoRoute(_IRoute.IRoute):
    @router.post("/api/aluno/endereco/", response_model=_enderecoSchema.Endereco)
    def criar(endereco: _enderecoSchema.EnderecoCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.inserir(db, endereco)

    @router.get("/api/aluno/endereco/", response_model=List[_enderecoSchema.Endereco])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.buscarTodos(db)

    @router.get("/api/aluno/endereco/{endereco_id}", response_model=_enderecoSchema.Endereco)
    def ler(endereco_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.buscar(db, endereco_id)

    @router.put("/api/aluno/endereco/", response_model=_enderecoSchema.Endereco)
    def atualizar(endereco: _enderecoSchema.Endereco, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.atualizar(db, endereco)

    @router.delete("/api/aluno/endereco/", response_model=_enderecoSchema.Endereco)
    def remover(endereco_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.remover(db, endereco_id)

class EnderecoProfessorRoute(_IRoute.IRoute):
    @router.post("/api/professor/endereco/", response_model=_enderecoSchema.Endereco)
    def criar(endereco: _enderecoSchema.EnderecoCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.inserir(db, endereco)

    @router.get("/api/professor/endereco/", response_model=List[_enderecoSchema.Endereco])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.buscarTodos(db)

    @router.get("/api/professor/endereco/{endereco_id}", response_model=_enderecoSchema.Endereco)
    def ler(endereco_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.buscar(db, endereco_id)

    @router.put("/api/professor/endereco/", response_model=_enderecoSchema.Endereco)
    def atualizar(endereco: _enderecoSchema.Endereco, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.atualizar(db, endereco)

    @router.delete("/api/professor/endereco/", response_model=_enderecoSchema.Endereco)
    def remover(endereco_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.remover(db, endereco_id)
