import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from typing import List
from ..models import campus as _campusModel, curso as _cursoModel

from .interface import ICampusDAO as _ICampusDAO


class CampusDAO(_ICampusDAO.ICampusDAO):
    def inserir(self, db: _orm.Session, campus: _campusModel.Campus):
        db.add(campus)
        db.commit()
        db.refresh(campus)

        return campus

    def atualizar(self, db: _orm.Session, campus: _campusModel.Campus):
        db.merge(campus)
        db.commit()
        db.refresh(campus)
        return campus

    def remover(self, db: _orm.Session, campus_id: int):
        campus_db: _campusModel.Campus = self.buscar(db, campus_id)
        db.delete(campus_db)
        db.commit()

        return campus_db

    def buscar(self, db: _orm.Session, campus_id: int) -> _campusModel.Campus:
        return db.query(_campusModel.Campus).filter(_campusModel.Campus.id_campus == campus_id).first()

    def buscarTodos(self, db: _orm.Session) -> List[_campusModel.Campus]:
        return db.query(_campusModel.Campus).all()

    def buscarCampusPorNome(self, db: _orm.Session, campus_nome: str):
        return (
            db.query(_campusModel.Campus)
            .filter(_campusModel.Campus.nome == campus_nome)
            .first()
        )

    def adicionarCurso(self, db: _orm.Session, campus_id: int, curso_id: int):
        campus_db: _campusModel.Campus = self.buscar(db, campus_id)
        curso_db: _cursoModel.Curso = self.buscar(db, curso_id)

        campus_db.cursos.append(curso_db)
        db.commit()
        db.refresh(campus_db)

        return curso_db
