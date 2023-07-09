from abc import ABC, abstractmethod

class ITelefoneDAO(ABC):
    @abstractmethod
    def inserir(db, telefone):
        pass

    @abstractmethod
    def atualizar(db, telefone):
        pass

    @abstractmethod
    def remover(db, telefone_id):
        pass

    @abstractmethod
    def buscar(db, telefone_id):
        pass

    @abstractmethod
    def buscarTodos(db):
        pass

    @abstractmethod
    def buscarPorDdd(db, ddd):
        pass
