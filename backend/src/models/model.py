import sqlalchemy as _sql

import backend.src.database.database as _database


class Endereco(_database.Base):
  __tablename__ = "endereco"
  id = _sql.Column(_sql.Integer, primary_key=True, index=True)
  logradouro = _sql.Column(_sql.String)
  local = _sql.Column(_sql.String)
  numero = _sql.Column(_sql.Integer)
  cep = _sql.Column(_sql.String)
  tipo = _sql.Column(_sql.String)


class Telefone(_database.Base):
  __tablename__ = "telefone"
  id = _sql.Column(_sql.Integer, primary_key=True, index=True)
  cod_pais = _sql.Column(_sql.Integer)
  ddd = _sql.Column(_sql.Integer)
  number = _sql.Column(_sql.Integer)


class Pessoa(_database.Base):
  __abstract__ = True
  id = _sql.Column(_sql.Integer, primary_key=True, index=True)
  nome = _sql.Column(_sql.String)
  sobrenome = _sql.Column(_sql.String)
  cpf = _sql.Column(_sql.String)
  sexo = _sql.Column(_sql.String)
  raca = _sql.Column(_sql.String)


class Aluno(Pessoa, _database.Base):
  __tablename__ = "aluno"
  data_ingresso = _sql.Column(_sql.Date)
  data_nascimento = _sql.Column(_sql.Date)
