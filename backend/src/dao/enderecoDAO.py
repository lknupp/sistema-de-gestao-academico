import sqlalchemy.orm as _orm
from typing import List

from .interface import IEnderecoDAO as _IEnderecoDAO
from ..models import endereco as _enderecoModel
from ..schemas import enderecoSchema as _enderecoSchema


class EnderecoAlunoDAO(_IEnderecoDAO.IEnderecoDAO):
    def inserir(
        self, db: _orm.Session, endereco: _enderecoModel.EnderecoAluno
    ) -> _enderecoSchema.Endereco:
        db.add(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco

    def atualizar(
        self, db: _orm.Session, endereco: _enderecoModel.EnderecoAluno
    ) -> _enderecoModel.EnderecoAluno:
        db.merge(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco

    def remover(
        self, db: _orm.Session, endereco_id: int
    ) -> _enderecoModel.EnderecoAluno:
        endereco = (
            db.query(_enderecoModel.EnderecoAluno)
            .filter(_enderecoModel.EnderecoAluno.id_endereco == endereco_id)
            .first()
        )
        db.delete(endereco)
        db.commit()
        return endereco

    def buscar(
        self, db: _orm.Session, endereco_id: int
    ) -> _enderecoModel.EnderecoAluno:
        endereco = (
            db.query(_enderecoModel.EnderecoAluno)
            .filter(_enderecoModel.EnderecoAluno.id_endereco == endereco_id)
            .first()
        )
        return endereco

    def buscarTodos(self, db: _orm.Session) -> List[_enderecoModel.EnderecoAluno]:
        enderecos = db.query(_enderecoModel.EnderecoAluno).all()
        return enderecos

    def buscarPorLogradouro(
        self, db: _orm.Session, logradouro: str
    ) -> _enderecoModel.EnderecoAluno:
        endereco = (
            db.query(_enderecoModel.EnderecoAluno)
            .filter(_enderecoModel.EnderecoAluno.logradouro == logradouro)
            .first()
        )
        return endereco


class EnderecoProfessorDAO(_IEnderecoDAO.IEnderecoDAO):
    def inserir(
        self, db: _orm.Session, endereco: _enderecoModel.EnderecoProfessor
    ) -> _enderecoSchema.Endereco:
        db.add(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco

    def atualizar(
        self, db: _orm.Session, endereco: _enderecoModel.EnderecoProfessor
    ) -> _enderecoModel.EnderecoProfessor:
        db.merge(endereco)
        db.commit()
        db.refresh(endereco)
        return endereco

    def remover(
        self, db: _orm.Session, endereco_id: int
    ) -> _enderecoModel.EnderecoProfessor:
        endereco = (
            db.query(_enderecoModel.EnderecoProfessor)
            .filter(_enderecoModel.EnderecoProfessor.id == endereco_id)
            .first()
        )
        db.delete(endereco)
        db.commit()
        return endereco

    def buscar(
        self, db: _orm.Session, endereco_id: int
    ) -> _enderecoModel.EnderecoProfessor:
        endereco = (
            db.query(_enderecoModel.EnderecoProfessor)
            .filter(_enderecoModel.EnderecoProfessor.id == endereco_id)
            .first()
        )
        return endereco

    def buscarTodos(self, db: _orm.Session) -> List[_enderecoModel.EnderecoProfessor]:
        enderecos = db.query(_enderecoModel.EnderecoProfessor).all()
        return enderecos

    def buscarPorLogradouro(
        self, db: _orm.Session, logradouro: str
    ) -> _enderecoModel.EnderecoProfessor:
        endereco = (
            db.query(_enderecoModel.EnderecoProfessor)
            .filter(_enderecoModel.EnderecoProfessor.logradouro == logradouro)
            .first()
        )
        return endereco
