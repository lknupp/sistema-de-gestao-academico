from abc import ABC, abstractmethod


class IOfertaController(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inserir(oferta):
        pass

    @abstractmethod
    def atualizar(oferta):
        pass

    @abstractmethod
    def remover(id_oferta):
        pass

    @abstractmethod
    def buscar(id_oferta):
        pass

    @abstractmethod
    def buscarTodos():
        pass
