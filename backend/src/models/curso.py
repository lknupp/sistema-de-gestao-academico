import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from ..database import database as _database
from .campus import rl_campus_curso


class Curso(_database.Base):
    __tablename__ = "curso"
    id_curso = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String, unique=True, index=True)
    campus = _orm.relationship(
        'Campus', secondary=rl_campus_curso, back_populates='cursos')
    disciplinas = _orm.relationship('Disciplina', backref='curso')
    alunos = _orm.relationship('Aluno', backref='curso')
    professores = _orm.relationship('Professor', backref='curso')
