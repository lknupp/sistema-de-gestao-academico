import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from dotenv import load_dotenv
import os
import json

load_dotenv()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("APP_USER")
PASSWORD = os.getenv("APP_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

postgres = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
sqlite = "sqlite:///./src/database/college.db"

json_file = open("./src/database/database.json", "r")
json_data = json.load(json_file)
if json_data["database"] == "sqlite":
    SQLALCHEMY_DATABASE_URL = sqlite
else:
    SQLALCHEMY_DATABASE_URL = postgres



engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)


# def create_function():
#     function_remove_prerequisito = _sql.DDL(
#         """
#     CREATE OR REPLACE FUNCTION remove_prerequisito()
#     RETURNS TRIGGER AS $$
#     BEGIN
#         DELETE FROM prerequisito p
#         WHERE id_disciplina = OLD.id_disciplina
#         OR disciplina_prerequisito = OLD.id_disciplina;
#         RETURN NULL;
#     END;
#     $$ LANGUAGE plpgsql;
# """
#     )

#     trigger_remover_prerequisito = _sql.DDL(
#         """
#     CREATE OR REPLACE TRIGGER remover_prerequisito
#     BEFORE DELETE ON disciplina
#     FOR EACH ROW
#     EXECUTE FUNCTION remove_prerequisito();
# """
#     )

#     function_remove_aluno_info = _sql.DDL(
#         """
#     CREATE OR REPLACE FUNCTION remove_aluno_info()
#     RETURNS TRIGGER AS $$
#     BEGIN
#         DELETE FROM telefone t WHERE id_telefone = OLD.id_telefone;
#         DELETE FROM endereco a WHERE id_endereco = OLD.id_endereco;
#         DELETE FROM historico h WHERE id_historico = OLD.id_historico;
#     END;
#     $$ LANGUAGE plpgsql;
# """
#     )

#     trigger_remover_aluno_info = _sql.DDL(
#         """
#     CREATE OR REPLACE TRIGGER remover_aluno_info
#     BEFORE DELETE ON aluno
#     FOR EACH ROW
#     EXECUTE FUNCTION remove_aluno_info();
# """
#     )

#     function_remove_professor_info = _sql.DDL(
#         """
#     CREATE OR REPLACE FUNCTION remove_professor_info()
#     RETURNS TRIGGER AS $$
#     BEGIN
#         DELETE FROM telefone t WHERE id_telefone = OLD.id_telefone;
#         DELETE FROM endereco a WHERE id_endereco = OLD.id_endereco;
#         DELETE FROM historico h WHERE id_historico = OLD.id_historico;
#     END;
#     $$ LANGUAGE plpgsql;
# """
#     )

#     trigger_remover_professor_info = _sql.DDL(
#         """
#     CREATE OR REPLACE TRIGGER remover_professor_info
#     BEFORE DELETE ON professor
#     FOR EACH ROW
#     EXECUTE FUNCTION remove_professor_info();
# """
#     )

#     view_visualizar_reprovados = _sql.DDL(
#         """
#     CREATE OR REPLACE VIEW visualizar_reprovados AS
#     SELECT a.nome, a.sobrenome, d.nome, h.nota, h.faltas
#     FROM aluno a
#     INNER JOIN rl_historico rh ON a.id_pessoa = rh.id_aluno_fk
#     INNER JOIN oferta o ON rh.id_oferta_fk = o.id_oferta
#     INNER JOIN disciplina d ON o.id_disciplina = d.id_disciplina
#     INNER JOIN historico h ON rh.id_historico = h.id_historico
#     WHERE h.nota < 6 OR h.faltas > 25;
# """
#     )

#     view_visualizar_aprovados = _sql.DDL(
#         """
#     CREATE OR REPLACE VIEW visualizar_aprovados AS
#     SELECT a.nome, a.sobrenome, d.nome, h.nota, h.faltas
#     FROM aluno a
#     INNER JOIN rl_historico rh ON a.id_pessoa = rh.id_aluno_fk
#     INNER JOIN oferta o ON rh.id_oferta_fk = o.id_oferta
#     INNER JOIN disciplina d ON o.id_disciplina = d.id_disciplina
#     INNER JOIN historico h ON rh.id_historico = h.id_historico
#     WHERE h.nota >= 6 AND h.faltas <= 25;
# """
#     )

#     procedure_visualizar_reprovados = _sql.DDL(
#         """
#     CREATE OR REPLACE PROCEDURE visualizar_reprovados()
#     LANGUAGE SQL
#     AS $$
#     SELECT * FROM visualizar_reprovados;
#     $$;
# """
#     )

#     procedure_visualizar_aprovados = _sql.DDL(
#         """
#     CREATE OR REPLACE PROCEDURE visualizar_aprovados()
#     LANGUAGE SQL
#     AS $$
#     SELECT * FROM visualizar_aprovados;
#     $$;
# """
#     )

    # with engine.connect() as conn:
    #     conn.execute(function_remove_prerequisito)
    #     conn.execute(trigger_remover_prerequisito)
    #     conn.commit()
