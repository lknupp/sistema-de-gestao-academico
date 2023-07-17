import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus

from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import alunoSchema as _alunoSchema
from ..controller import alunoController as _controller

router = _fastapi.APIRouter()
controller = _controller.AlunoController()
tags_metadata = [
    {
        "name": "aluno",
        "description": "",
    }
]


class AlunoRoute(_IRoute.IRoute):
    @router.post(
        "/api/aluno/",
        response_model=_alunoSchema.Aluno,
        status_code=HTTPStatus.CREATED.value,
        description=HTTPStatus.CREATED.phrase,
        tags=["aluno"],
    )
    def criar(
        aluno: _alunoSchema.AlunoCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        controller.buscarPorCPF(db, cpf=aluno.cpf)
        return controller.inserir(db, aluno)

    @router.get("/api/aluno/", response_model=List[_alunoSchema.Aluno], tags=["aluno"])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarTodos(db)

    @router.get(
        "/api/aluno/id/{id_aluno}", response_model=_alunoSchema.Aluno, tags=["aluno"]
    )
    def ler(id_aluno: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscar(db, id_aluno)

    @router.get(
        "/api/aluno/cpf/{cpf}", response_model=_alunoSchema.Aluno, tags=["aluno"]
    )
    def ler_por_cpf(cpf: str, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.buscarPorCPF(db, cpf)

    @router.put("/api/aluno/", response_model=_alunoSchema.Aluno, tags=["aluno"])
    def atualizar(
        aluno: _alunoSchema.Aluno, db: _orm.Session = _fastapi.Depends(_database.get_db)
    ):
        return controller.atualizar(db, aluno)

    @router.delete("/api/aluno/", response_model=_alunoSchema.Aluno, tags=["aluno"])
    def remover(id_aluno: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, id_aluno)
