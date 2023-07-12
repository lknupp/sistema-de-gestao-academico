import fastapi as _fastapi
import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus

from .interface import IRoute as _IRoute
from ..database import database as _database
from ..schemas import campusSchema as _campusSchema, cursoSchema as _cursoSchema
from ..controller import campusController as _controller

router = _fastapi.APIRouter()
controller = _controller.CampusController()


class CampusRoute(_IRoute.IRoute):
    @router.post("/api/campus/", response_model=_campusSchema.Campus, status_code=HTTPStatus.CREATED.value, description=HTTPStatus.CREATED.phrase)
    def criar(
        campus: _campusSchema.CampusCreate,
        db: _orm.Session = _fastapi.Depends(_database.get_db),
    ):
        db_campus = controller.buscarCampusPorNome(db, campus_nome=campus.nome)
        if db_campus:
            raise _fastapi.HTTPException(
                status_code=400, detail="Campus já cadastrado.")
        return controller.inserir(db, campus)

    @router.get("/api/campus/", response_model=List[_campusSchema.Campus])
    def ler_todos(db: _orm.Session = _fastapi.Depends(_database.get_db)):
        campus = controller.buscarTodos(db)
        if campus is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Não existem campuss cadastrados."
            )
        return campus

    @router.get("/api/campus/campus-id/{campus_id}", response_model=_campusSchema.Campus)
    def ler(campus_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        campus = controller.buscar(db, campus_id)
        if campus is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Campus não encontrado")
        return campus

    @router.get("/api/campus/campus-nome/{campus_nome}", response_model=_campusSchema.Campus)
    def ler(campus_nome: str, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        campus = controller.buscarCampusPorNome(db, campus_nome)
        if campus is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Campus não encontrado")
        return campus

    @router.put("/api/campus/atualizar/", response_model=_campusSchema.Campus)
    def atualizar(campus: _campusSchema.Campus, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.atualizar(db, campus)

    @router.delete("/api/campus/remover/", response_model=_campusSchema.Campus)
    def remover(campus_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.remover(db, campus_id)

    @router.post("/api/campus/adicionar-curso/", response_model=_campusSchema.Campus)
    def adicionar_curso(campus_id: int, curso_id: int, db: _orm.Session = _fastapi.Depends(_database.get_db)):
        return controller.adicionarCurso(db, campus_id, curso_id)
