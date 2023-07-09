from abc import ABC, abstractmethod


class IPessoaController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(pessoa):
        pass

    @abstractmethod
    def atualizar(pessoa):
        pass

    @abstractmethod
    def remover(pessoa_id):
        pass

    @abstractmethod
    def buscar(pessoa_id):
        pass

    @abstractmethod
    def buscarPorCPF(cpf):
        pass
