from abc import ABC, abstractmethod


class IDisciplinaDAO(ABC):
    @abstractmethod
    def inserir(db, disciplina):
        pass

    @abstractmethod
    def atualizar(db, disciplina):
        pass

    @abstractmethod
    def remover(db, disciplina_id):
        pass

    @abstractmethod
    def buscar(db):
        pass
