import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List

import backend.src.database.database as _database
from src.schemas import pessoaSchema as _schemas
import src.controller.pessoaController as _controller

router = _fastapi.APIRouter()

controller = _controller.AlunoController()

@router.post("/api/aluno/", response_model=_schemas.Aluno)
def criar_aluno(aluno: _schemas.AlunoCreate,
                db: _orm.Session = _fastapi.Depends(_database.get_db)):
  db_aluno = controller.buscarPorCPF(db, cpf=aluno.cpf)
  if db_aluno:
    raise _fastapi.HTTPException(status_code=400, detail="CPF já cadastrado.")

  return controller.inserir(db, aluno=aluno)



@router.get("/api/aluno/", response_model=List[_schemas.Aluno])
def ler_alunos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
  alunos = controller.buscarTodos(db)
  if alunos is None:
    raise _fastapi.HTTPException(status_code=404,
                                 detail="Alunos não encontrados")
  return alunos


@router.get("/api/aluno/{aluno_id}", response_model=_schemas.Aluno)
def ler_aluno(aluno_id: int,
              db: _orm.Session = _fastapi.Depends(_database.get_db)):
  aluno = controller.buscar(db, aluno_id)
  if aluno is None:
    raise _fastapi.HTTPException(status_code=404,
                                 detail="Aluno não encontrado")
  return aluno
