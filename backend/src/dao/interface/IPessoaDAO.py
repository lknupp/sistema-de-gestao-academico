from abc import ABC, abstractmethod


class IPessoaDAO(ABC):
    @abstractmethod
    def inserir(db, pessoa):
        pass

    @abstractmethod
    def atualizar(db, pessoa):
        pass

    @abstractmethod
    def remover(db, pessoa_id):
        pass

    @abstractmethod
    def buscar(db, pessoa_id):
        pass
