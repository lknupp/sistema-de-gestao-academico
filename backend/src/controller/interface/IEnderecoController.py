from abc import ABC, abstractmethod


class IEnderecoController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(endereco):
        pass

    @abstractmethod
    def atualizar(endereco):
        pass

    @abstractmethod
    def remover(endereco_id):
        pass

    @abstractmethod
    def buscar(endereco_id):
        pass

    @abstractmethod
    def buscarTodos():
        pass

    @abstractmethod
    def buscarPorLogradouro(logradouro):
        pass
