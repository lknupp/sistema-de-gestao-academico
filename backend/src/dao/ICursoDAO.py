from abc import ABC, abstractmethod


class ICursoDAO(ABC):
    @abstractmethod
    def inserir(db, curso):
        pass

    @abstractmethod
    def atualizar(db, curso):
        pass

    @abstractmethod
    def remover(db, curso_id):
        pass

    @abstractmethod
    def buscarTodos(db):
        pass

    @abstractmethod
    def buscarCursoPorNome(db, curso_id):
        pass
