from abc import ABC, abstractmethod


class ICampusController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(campus):
        pass

    @abstractmethod
    def atualizar(campus):
        pass

    @abstractmethod
    def remover(campus_id):
        pass

    @abstractmethod
    def buscar(campus_id):
        pass

    @abstractmethod
    def buscarTodos():
        pass

    @abstractmethod
    def buscarCampusPorNome(campus_nome):
        pass
