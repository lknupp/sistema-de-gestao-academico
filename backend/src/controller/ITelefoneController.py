from abc import ABC, abstractmethod


class ITelefoneController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(telefone):
        pass

    @abstractmethod
    def atualizar(telefone):
        pass

    @abstractmethod
    def remover(telefone_id):
        pass

    @abstractmethod
    def buscar(telefone_id):
        pass

    @abstractmethod
    def buscarTodos():
        pass

    @abstractmethod
    def buscarPorDdd(ddd):
        pass
