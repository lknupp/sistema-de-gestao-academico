import sqlalchemy.orm as _orm
from typing import List
from ..models import oferta as _ofertaModel
from .interface import IOfertaDAO as _IOfertaDAO


class OfertaDAO(_IOfertaDAO.IOfertaDAO):
    def inserir(self, db: _orm.Session, oferta: _ofertaModel.Oferta):
        db.add(oferta)
        db.commit()
        db.refresh(oferta)
        return oferta

    def atualizar(self, db: _orm.Session, oferta: _ofertaModel.Oferta):
        db.merge(oferta)
        db.commit()
        db.refresh(oferta)
        return oferta

    def remover(self, db: _orm.Session, oferta: _ofertaModel.Oferta):
        db.delete(oferta)
        db.commit()
        return oferta

    def buscar(self, db: _orm.Session, oferta_id: int) -> _ofertaModel.Oferta:
        return (
            db.query(_ofertaModel.Oferta)
            .filter(_ofertaModel.Oferta.id_oferta == oferta_id)
            .first()
        )

    def buscarTodos(self, db: _orm.Session) -> List[_ofertaModel.Oferta]:
        return db.query(_ofertaModel.Oferta).all()

    # def adicionar_historico():

    # def buscar_historico():

    # def atualizar_historico():
