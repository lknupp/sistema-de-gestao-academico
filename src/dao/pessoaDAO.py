from typing import List, Optional
import sqlalchemy.orm as _orm
import src.model as _model
import src.schemas.mensagemSchema as _schemas


class IPessoaDAO:
    def inserir(db: _orm.Session, pessoa: _model.Pessoa) -> _model.Pessoa:
        pass

    def atualizar_dados(db: _orm.Session, pessoa: _model.Pessoa) -> _model.Pessoa:
        pass

    def remover(db: _orm.Session, id: int) -> bool:
        pass

    def buscar(db: _orm.Session, id: int) -> _model.Pessoa:
        pass


class AlunoDAO(IPessoaDAO):
    def inserir(self, db: _orm.Session, aluno: _model.Aluno) -> _schemas.Mensagem:
        mensagem = _schemas.Mensagem()
        try:
            db.add(aluno)
            db.commit()
            db.refresh(aluno)
            mensagem.id = aluno.id
            mensagem.texto = "Aluno cadastrado com sucesso!"
        except Exception as e:
            mensagem.id = -1
            mensagem.texto = "Erro ao cadastrar aluno.\n{}".format(e)
        return mensagem

    def atualizar_dados(
        self, db: _orm.Session, aluno: _model.Aluno
    ) -> _schemas.Mensagem:
        mensagem = _schemas.Mensagem()
        try:
            db.query(_model.Aluno).filter(_model.Aluno.id == aluno.id).update(aluno)
            db.commit()
            db.refresh(aluno)
            mensagem.id = aluno.id
            mensagem.texto = "Dados do aluno atualizados com sucesso!"
        except Exception as e:
            mensagem.id = -1
            mensagem.texto = "Erro ao atualizar dados do aluno.\n{}".format(e)
        return mensagem

    def remover(self, db: _orm.Session, id: int) -> _schemas.Mensagem:
        mensagem = _schemas.Mensagem()
        try:
            db.remove(db.query(_model.Aluno).filter(_model.Aluno.id == id).first())
            db.commit()
            mensagem.id = id
            mensagem.texto = "Aluno removido com sucesso!"
        except Exception as e:
            mensagem.id = -1
            mensagem.texto = "Erro ao remover aluno.\n{}".format(e)
        return mensagem

    def buscar(self, db: _orm.Session, id: int) -> _model.Aluno:
        aluno = db.query(_model.Aluno).filter(_model.Aluno.id == id).first()
        return aluno

    def buscarTodos(self, db: _orm.Session) -> List[_model.Aluno]:
        alunos = db.query(_model.Aluno).all()
        return alunos

    def buscarPorCPF(self, db: _orm.Session, cpf: str) -> _model.Aluno:
        aluno = db.query(_model.Aluno).filter(_model.Aluno.cpf == cpf).first()
        return aluno

    def filtrarPorAno(self, db: _orm.Session, ano: int) -> List[_model.Aluno]:
        alunos = db.query(_model.Aluno).filter(_model.Aluno.ano == ano).all()
        return alunos
