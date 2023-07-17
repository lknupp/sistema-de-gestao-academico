import sqlalchemy.orm as _orm
from typing import List

from .interface import IOfertaController as _ofertaController
from ..dao import ofertaDAO as _ofertaDAO
from ..schemas import ofertaSchema as _ofertaSchema
from ..models import oferta as _ofertaModel


class OfertaController(_ofertaController.IOfertaController):
    def __init__(self) -> None:
        super().__init__()
        self.oferta_dao = _ofertaDAO.OfertaDAO()

    def inserir(
        self, db: _orm.Session, oferta: _ofertaSchema.OfertaCreate
    ) -> _ofertaSchema.Oferta:
        res = _ofertaModel.Oferta(**oferta.model_dump())
        return self.oferta_dao.inserir(db, res)

    def atualizar(
        self, db: _orm.Session, oferta: _ofertaSchema.Oferta
    ) -> _ofertaSchema.Oferta:
        res = _ofertaModel.Oferta(**oferta.model_dump())
        return self.oferta_dao.atualizar(db, res)

    def remover(self, db: _orm.Session, id_oferta: int) -> _ofertaSchema.Oferta:
        res = self.oferta_dao.remover(db, id_oferta)
        return res

    def buscar(self, db: _orm.Session, id_oferta: int) -> _ofertaSchema.Oferta:
        res = self.oferta_dao.buscar(db, id_oferta)
        return res

    def buscarTodos(self, db: _orm.Session) -> List[_ofertaSchema.Oferta]:
        res = self.oferta_dao.buscarTodos(db)
        return res
