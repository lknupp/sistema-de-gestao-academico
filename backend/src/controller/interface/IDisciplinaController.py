from abc import ABC, abstractmethod


class IDisciplinaController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(disciplina):
        pass

    @abstractmethod
    def atualizar(disciplina):
        pass

    @abstractmethod
    def remover(id_disciplina):
        pass

    @abstractmethod
    def buscar(id_disciplina):
        pass

    @abstractmethod
    def buscarTodos():
        pass
