import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List

from . import IRoute as _IRoute
from ..database import sqlite as _database
from ..schemas import alunoSchema as _alunoSchema
from ..controller import alunoController as _controller

router = _fastapi.APIRouter()
controller = _controller.AlunoController()


class AlunoRoute(_IRoute.IRoute):
    @router.post("/api/aluno/", response_model=_alunoSchema.Aluno)
    def criar(
        aluno: _alunoSchema.AlunoCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        db_aluno = controller.buscarPorCPF(db, cpf=aluno.cpf)
        if db_aluno:
            raise _fastapi.HTTPException(status_code=400, detail="CPF já cadastrado.")
        return controller.inserir(db, aluno)

    @router.get("/api/aluno/", response_model=List[_alunoSchema.Aluno])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        alunos = controller.buscarTodos(db)
        if alunos is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Alunos não encontrados"
            )
        return alunos

    @router.get("/api/aluno/{aluno_id}", response_model=_alunoSchema.Aluno)
    def ler(aluno_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        aluno = controller.buscar(db, aluno_id)
        if aluno is None:
            raise _fastapi.HTTPException(status_code=404, detail="Aluno não encontrado")
        return aluno
