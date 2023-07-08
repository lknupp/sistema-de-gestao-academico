import sqlalchemy.orm as _orm
from typing import List

from . import IEnderecoController as _enderecoController
from ..dao import enderecoDAO as _enderecoDAO
from ..schemas import enderecoSchema as _enderecoSchema
from ..schemas import mensagemSchema as _msgSchema
from ..models import endereco as _enderecoModel

class EnderecoController(_enderecoController.IEnderecoController):
    def __init__(self) -> None:
        super().__init__()
        self.endereco_dao = _enderecoDAO.EnderecoDAO()
    
    def inserir(self, db: _orm.Session, endereco: _enderecoSchema.EnderecoCreate) -> _msgSchema.Mensagem:
        endereco_db = _enderecoModel.Endereco(**endereco.dict())
        return self.endereco_dao.inserir(db, endereco_db)
    
    def atualizar(self, db: _orm.Session, endereco: _enderecoSchema.Endereco) -> _msgSchema.Mensagem:
        endereco_db = _enderecoModel.Endereco(**endereco.dict())
        return self.endereco_dao.atualizar(db, endereco_db)
    
    def remover(self, db: _orm.Session, endereco: _enderecoSchema.Endereco) -> _msgSchema.Mensagem:
        endereco_db = _enderecoModel.Endereco(**endereco.dict())
        return self.endereco_dao.remover(db, endereco_db)
    
    def buscar(self, db: _orm.Session, endereco_id: int) -> _enderecoSchema.Endereco:
        return self.endereco_dao.buscar(db, endereco_id)
    
    def buscarTodos(self, db: _orm.Session) -> List[_enderecoSchema.Endereco]:
        return self.endereco_dao.buscarTodos(db)
    
    def buscarPorLogradouro(self, db: _orm.Session, logradouro: str) -> List[_enderecoSchema.Endereco]:
        return self.endereco_dao.buscarPorLogradouro(db, logradouro)
