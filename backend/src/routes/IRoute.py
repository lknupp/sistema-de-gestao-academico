from abc import ABC, abstractmethod


class IRoute(ABC):
    @abstractmethod
    def criar(self, objeto, db):
        pass

    @abstractmethod
    def ler(self, objeto_id, db):
        pass

    @abstractmethod
    def ler_todos(self, db):
        pass

    @abstractmethod
    def atualizar(self, objeto, db):
        pass

    @abstractmethod
    def deletar(self, objeto_id, db):
        pass
