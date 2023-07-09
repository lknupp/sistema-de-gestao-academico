import sqlalchemy.orm as _orm
from typing import List

from . import IEnderecoDAO as _IEnderecoDAO
from ..models import endereco as _enderecoModel
from ..schemas import enderecoSchema as _enderecoSchema

class EnderecoDAO(_IEnderecoDAO.IEnderecoDAO):
    def inserir(self, db: _orm.Session, endereco: _enderecoModel.Endereco) -> _enderecoSchema.Endereco:
        db.add(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco
    
    def atualizar(self, db: _orm.Session, endereco: _enderecoModel.Endereco) -> _enderecoModel.Endereco:
        db.query(_enderecoModel.Endereco).filter(_enderecoModel.Endereco.id == endereco.id).update(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco
    
    def remover(self, db: _orm.Session, endereco_id: int) -> _enderecoModel.Endereco:
        endereco = db.query(_enderecoModel.Endereco).filter(_enderecoModel.Endereco.id == endereco_id).first()
        db.remove(endereco)
        db.commit()
        return endereco
    
    def buscar(self, db: _orm.Session, endereco_id: int) -> _enderecoModel.Endereco:
        endereco = db.query(_enderecoModel.Endereco).filter(_enderecoModel.Endereco.id == endereco_id).first()
        return endereco
    
    def buscarTodos(self, db: _orm.Session) -> List[_enderecoModel.Endereco]:
        enderecos = db.query(_enderecoModel.Endereco).all()
        return enderecos
    
    def buscarPorLogradouro(self, db: _orm.Session, logradouro: str) -> _enderecoModel.Endereco:
        endereco = db.query(_enderecoModel.Endereco).filter(_enderecoModel.Endereco.logradouro == logradouro).first()
        return endereco
