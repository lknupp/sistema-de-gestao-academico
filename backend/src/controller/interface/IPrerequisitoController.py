from abc import ABC, abstractmethod


class IPrerequisitoController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(prerequisito):
        pass

    @abstractmethod
    def atualizar(prerequisito):
        pass

    @abstractmethod
    def remover(id_prerequisito):
        pass

    @abstractmethod
    def buscar(id_prerequisito):
        pass
