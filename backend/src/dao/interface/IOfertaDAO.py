from abc import ABC, abstractmethod


class IOfertaDAO(ABC):
    @abstractmethod
    def inserir(db, oferta):
        pass

    @abstractmethod
    def atualizar(db, oferta):
        pass

    @abstractmethod
    def remover(db, oferta_id):
        pass

    @abstractmethod
    def buscar(db):
        pass
