import sqlalchemy.orm as _orm
from typing import List

from ..models import prerequisito as _prerequisitoModel
from ..schemas import prerequisitoSchema as _prerequisitoSchema
from .interface import IPrerequisitoDAO as _IPrerequisitoDAO


class PrerequisitoDAO(_IPrerequisitoDAO.IPrerequisitoDAO):
    def inserir(
        self, db: _orm.Session, prerequisito: _prerequisitoModel.Prerequisito
    ) -> _prerequisitoSchema.Prerequisito:
        db.add(prerequisito)
        db.commit()
        db.refresh(prerequisito)
        return prerequisito

    def atualizar(
        self, db: _orm.Session, prerequisito: _prerequisitoModel.Prerequisito
    ) -> _prerequisitoSchema.Prerequisito:
        db.merge(prerequisito)
        db.commit()
        db.refresh(prerequisito)
        return prerequisito

    def remover(
        self, db: _orm.Session, id_prerequisito: int
    ) -> _prerequisitoSchema.Prerequisito:
        prerequisito = (
            db.query(_prerequisitoModel.Prerequisito)
            .filter(_prerequisitoModel.Prerequisito.id_prerequisito == id_prerequisito)
            .first()
        )
        db.delete(prerequisito)
        db.commit()
        return prerequisito

    def buscar(
        self, db: _orm.Session, id_prerequisito: int
    ) -> _prerequisitoModel.Prerequisito:
        prerequisito = (
            db.query(_prerequisitoModel.Prerequisito)
            .filter(_prerequisitoModel.Prerequisito.id_prerequisito == id_prerequisito)
            .first()
        )
        return prerequisito
