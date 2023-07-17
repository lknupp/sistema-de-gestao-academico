from abc import ABC, abstractmethod


class ICampusDAO(ABC):
    @abstractmethod
    def inserir(db, campus):
        pass

    @abstractmethod
    def atualizar(db, campus):
        pass

    @abstractmethod
    def remover(db, campus_id):
        pass

    @abstractmethod
    def buscarTodos(db):
        pass

    @abstractmethod
    def buscarCampusPorNome(db, campus_id):
        pass
