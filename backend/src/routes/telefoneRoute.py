import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus
from .interface import IRoute as _IRoute
from ..database import sqlite as _database
from ..schemas import telefoneSchema as _telefoneSchema
from ..controller import telefoneController as _controller

router = _fastapi.APIRouter()
controllerAluno = _controller.TelefoneController("aluno")
controllerProfessor = _controller.TelefoneController("professor")


class TelefoneAlunoRoute(_IRoute.IRoute):
    @router.post("/api/aluno/telefone/", response_model=_telefoneSchema.Telefone, status_code=HTTPStatus.CREATED.value, description=HTTPStatus.CREATED.phrase)
    def criar(telefone: _telefoneSchema.TelefoneCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.inserir(db, telefone)

    @router.get("/api/aluno/telefone/", response_model=List[_telefoneSchema.Telefone])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.buscarTodos(db)

    @router.get("/api/aluno/telefone/{telefone_id}", response_model=_telefoneSchema.Telefone)
    def ler(telefone_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.buscar(db, telefone_id)

    @router.put("/api/aluno/telefone/", response_model=_telefoneSchema.Telefone)
    def atualizar(telefone: _telefoneSchema.Telefone, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.atualizar(db, telefone)

    @router.delete("/api/aluno/telefone/", response_model=_telefoneSchema.Telefone)
    def remover(telefone_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerAluno.remover(db, telefone_id)


class TelefoneProfessorRoute(_IRoute.IRoute):
    @router.post("/api/professor/telefone/", response_model=_telefoneSchema.Telefone)
    def criar(telefone: _telefoneSchema.TelefoneCreate, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.inserir(db, telefone)

    @router.get("/api/professor/telefone/", response_model=List[_telefoneSchema.Telefone])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.buscarTodos(db)

    @router.get("/api/professor/telefone/{telefone_id}", response_model=_telefoneSchema.Telefone)
    def ler(telefone_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.buscar(db, telefone_id)

    @router.put("/api/professor/telefone/", response_model=_telefoneSchema.Telefone)
    def atualizar(telefone: _telefoneSchema.Telefone, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.atualizar(db, telefone)

    @router.delete("/api/professor/telefone/", response_model=_telefoneSchema.Telefone)
    def remover(telefone_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controllerProfessor.remover(db, telefone_id)
