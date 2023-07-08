from abc import ABC, abstractmethod

class IEnderecoDAO(ABC):
    @abstractmethod
    def inserir(db, endereco):
        pass

    @abstractmethod
    def atualizar(db, endereco):
        pass

    @abstractmethod
    def remover(db, endereco_id):
        pass

    @abstractmethod
    def buscar(db, endereco_id):
        pass

    @abstractmethod
    def buscarTodos(db):
        pass

    @abstractmethod
    def buscarPorLogradouro(db, logradouro):
        pass
