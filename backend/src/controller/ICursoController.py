from abc import ABC, abstractmethod


class ICursoController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(curso):
        pass

    @abstractmethod
    def atualizar(curso):
        pass

    @abstractmethod
    def remover(curso_id):
        pass

    @abstractmethod
    def buscar(curso_id):
        pass

    @abstractmethod
    def buscarTodos():
        pass

    @abstractmethod
    def buscarCursoPorNome(curso_nome):
        pass
