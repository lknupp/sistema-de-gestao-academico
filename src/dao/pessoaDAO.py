from typing import List, Optional
import sqlalchemy.orm as _orm
import src.model as _model


class IPessoaDAO:

  def inserir(db: _orm.Session, pessoa: _model.Pessoa) -> bool:
    pass

  def atualizarDados(db: _orm.Session, pessoa: _model.Pessoa) -> bool:
    pass

  def remover(db: _orm.Session, id: int) -> bool:
    pass

  def buscar(db: _orm.Session, id: int) -> _model.Pessoa:
    pass


class AlunoDAO(IPessoaDAO):

  def inserir(self, db: _orm.Session, aluno: _model.Aluno) -> Optional[_model.Aluno]:
    try:
      db.add(aluno)
      db.commit()
      db.refresh(aluno)
      return aluno
    except:
      return None

  def atualizarDados(self, db: _orm.Session, aluno: _model.Aluno) -> bool:
    try:
      db.query(_model.Aluno).filter(_model.Aluno.id == aluno.id).update(aluno)
      db.commit()
      return True
    except:
      return False

  def remover(self, db: _orm.Session, id: int) -> bool:
    try:
      db.remove(db.query(_model.Aluno).filter(_model.Aluno.id == id).first())
      db.commit()
      return True
    except:
      return False

  def buscar(self, db: _orm.Session, id: int) -> _model.Aluno:
    try:
      aluno = db.query(_model.Aluno).filter(_model.Aluno.id == id).first()
      return aluno
    except:
      return None

  def buscarTodos(self, db: _orm.Session) -> List[_model.Aluno]:
    try:
      alunos = db.query(_model.Aluno).all()
      return alunos
    except:
      return None

  def buscarPorCPF(self, db: _orm.Session, cpf: str) -> Optional[_model.Aluno]:
    try:
      aluno = db.query(_model.Aluno).filter(_model.Aluno.cpf == cpf).first()
      return aluno
    except:
      return None

  def filtrarPorAno(self, db: _orm.Session, ano: int) -> List[_model.Aluno]:
    try:
      alunos = db.query(_model.Aluno).filter(_model.Aluno.ano == ano).all()
      return alunos
    except:
      return None
