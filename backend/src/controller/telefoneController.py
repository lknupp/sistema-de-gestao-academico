import sqlalchemy.orm as _orm
from typing import List

from . import ITelefoneController as _telefoneController
from ..dao import telefoneDAO as _telefoneDAO
from ..schemas import telefoneSchema as _telefoneSchema
from ..models import telefone as _telefoneModel

class TelefoneController(_telefoneController.ITelefoneController):
    def __init__(self, model) -> None:
        super().__init__()
        if model == 'aluno':
            self.telefone_dao = _telefoneDAO.TelefoneAlunoDAO()
            self.model = _telefoneModel.TelefoneAluno
        elif model == 'professor':
            self.telefone_dao = _telefoneDAO.TelefoneProfessorDAO()
            self.model = _telefoneModel.TelefoneProfessor
    
    def inserir(self, db: _orm.Session, telefone: _telefoneSchema.TelefoneCreate) -> _telefoneSchema.Telefone:
        telefone_db = self.model(**telefone.dict())
        return self.telefone_dao.inserir(db, telefone_db)
    
    def atualizar(self, db: _orm.Session, telefone: _telefoneSchema.Telefone) -> _telefoneSchema.Telefone:
        telefone_db = self.model(**telefone.dict())
        return self.telefone_dao.atualizar(db, telefone_db)
    
    def remover(self, db: _orm.Session, telefone: _telefoneSchema.Telefone) -> _telefoneSchema.Telefone:
        telefone_db = self.model(**telefone.dict())
        return self.telefone_dao.remover(db, telefone_db)
    
    def buscar(self, db: _orm.Session, telefone_id: int) -> _telefoneSchema.Telefone:
        return self.telefone_dao.buscar(db, telefone_id)
    
    def buscarTodos(self, db: _orm.Session) -> List[_telefoneSchema.Telefone]:
        return self.telefone_dao.buscarTodos(db)
    
    def buscarPorDdd(self, db: _orm.Session, ddd: int) -> List[_telefoneSchema.Telefone]:
        return self.telefone_dao.buscarPorLogradouro(db, ddd)
