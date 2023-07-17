from abc import ABC, abstractmethod


class IPrerequisitoDAO(ABC):
    @abstractmethod
    def inserir(db, prerequisito):
        pass

    @abstractmethod
    def atualizar(db, prerequisito):
        pass

    @abstractmethod
    def remover(db, prerequisito_id):
        pass

    @abstractmethod
    def buscar(db):
        pass
