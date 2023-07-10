import sqlalchemy.orm as _orm

from .interface import IPrerequisitoController as _prerequisitoController
from ..dao import prerequisitoDAO as _prerequisitoDAO
from ..schemas import prerequisitoSchema as _prerequisitoSchema
from ..models import prerequisito as _prerequisitoModel


class PrerequisitoController(_prerequisitoController.IPrerequisitoController):
    def __init__(self) -> None:
        super().__init__()
        self.prerequisito_dao = _prerequisitoDAO.PrerequisitoDAO()

    def inserir(self, db: _orm.Session, prerequisito: _prerequisitoSchema.PrerequisitoCreate) -> _prerequisitoSchema.Prerequisito:
        res = _prerequisitoModel.Prerequisito(**prerequisito.model_dump())
        return self.prerequisito_dao.inserir(db, res)

    def atualizar(self, db: _orm.Session, prerequisito: _prerequisitoSchema.Prerequisito) -> _prerequisitoSchema.Prerequisito:
        res = _prerequisitoModel.Prerequisito(**prerequisito.model_dump())
        return self.prerequisito_dao.atualizar(db, res)

    def remover(self, db: _orm.Session, id_prerequisito: int) -> _prerequisitoSchema.Prerequisito:
        res = self.prerequisito_dao.remover(db, id_prerequisito)
        return res

    def buscar(self, db: _orm.Session, id_prerequisito: int) -> _prerequisitoSchema.Prerequisito:
        res = self.prerequisito_dao.buscar(db, id_prerequisito)
        return res