import sqlalchemy.orm as _orm
from typing import List
from http import HTTPStatus
import fastapi as _fastapi
from .interface import ICampusController as _ICampusController
from ..dao import campusDAO as _campusDAO
from ..dao import cursoDAO as _cursoDAO
from ..schemas import campusSchema as _campusSchema
from ..models import campus as _campusModel


class CampusController(_ICampusController.ICampusController):
    def __init__(self):
        super().__init__()
        self.campus_dao = _campusDAO.CampusDAO()

    # TODO: Implementar Erros
    def inserir(self, db: _orm.Session, campus: _campusSchema.CampusCreate):
        db_campus = _campusModel.Campus(**campus.dict())
        try:
            campus = self.campus_dao.inserir(db=db, campus=db_campus)
        except Exception as e:
            pass
        return campus

    def atualizar(self, db: _orm.Session, campus: _campusSchema.CampusCreate):
        campus = _campusModel.Campus(**campus.dict())
        if campus is None:
            raise _fastapi.HTTPException(
                status_code=404, detail="Campus não encontrado"
            )
        try:
            campus = self.campus_dao.atualizar(db, campus)
        except Exception as e:
            pass
        return campus

    def remover(self, db: _orm.Session, campus_id: int):
        try:
            return self.campus_dao.remover(db, campus_id)
        except Exception as e:
            pass

    def buscar(self, db: _orm.Session, campus_id: int):
        return self.campus_dao.buscar(db=db, campus_id=campus_id)

    def buscarTodos(self, db: _orm.Session):
        return self.campus_dao.buscarTodos(db)

    def buscarCampusPorNome(self, db: _orm.Session, campus_nome: str):
        campus_db: _campusModel.Campus = self.campus_dao.buscarCampusPorNome(
            db=db, campus_nome=campus_nome
        )
        # if campus_db is None:
        #     raise _fastapi.HTTPException(
        #         status_code=HTTPStatus.NO_CONTENT.value, detail=HTTPStatus.NO_CONTENT.phrase)
        return campus_db

    def adicionarCurso(self, db, campus_id, curso_id):
        campus_db = self.campus_dao.buscar(db, campus_id)
        curso_db = _cursoDAO.CursoDAO().buscar(db, curso_id)
        return self.campus_dao.adicionarCurso(db, campus_db, curso_db)
