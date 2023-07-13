import sqlalchemy.orm as _orm
from typing import List

from .interface import ITelefoneDAO as _ITelefoneDAO
from ..models import telefone as _telefoneModel
from ..schemas import telefoneSchema as _telefoneSchema


class TelefoneDAO(_ITelefoneDAO.ITelefoneDAO):
    def inserir(self, db: _orm.Session, telefone: _telefoneModel.Telefone) -> _telefoneSchema.Telefone:
        db.add(telefone)
        db.commit()
        db.refresh(telefone)
        return telefone

    def atualizar(self, db: _orm.Session, telefone: _telefoneModel.Telefone) -> _telefoneModel.Telefone:
        db.merge(telefone)
        db.commit()
        db.refresh(telefone)
        return telefone

    def remover(self, db: _orm.Session, id_telefone: int) -> _telefoneModel.Telefone:
        telefone = (
            db.query(_telefoneModel.Telefone)
            .filter(_telefoneModel.Telefone.id_telefone == id_telefone)
            .first()
        )
        db.delete(telefone)
        db.commit()
        return telefone

    def buscar(self, db: _orm.Session, id_telefone: int) -> _telefoneModel.Telefone:
        telefone = (
            db.query(_telefoneModel.Telefone)
            .filter(_telefoneModel.Telefone.id_telefone == id_telefone)
            .first()
        )
        return telefone

    def buscarTodos(self, db: _orm.Session) -> List[_telefoneModel.Telefone]:
        telefones = db.query(_telefoneModel.Telefone).all()
        return telefones

    def buscarPorDdd(self, db: _orm.Session, ddd: int) -> _telefoneModel.Telefone:
        telefone = (
            db.query(_telefoneModel.Telefone)
            .filter(_telefoneModel.Telefone.ddd == ddd)
            .first()
        )
        return telefone
