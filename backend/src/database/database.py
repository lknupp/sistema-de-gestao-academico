import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("APP_USER")
PASSWORD = os.getenv("APP_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)

def create_function():
    function_remove_prerequisito = _sql.DDL(
    """
    CREATE OR REPLACE FUNCTION remove_prerequisito()
    RETURNS TRIGGER AS $$
    BEGIN
        DELETE FROM prerequisito p 
        WHERE id_disciplina = OLD.id_disciplina 
        OR disciplina_prerequisito = OLD.id_disciplina;
        RETURN NULL;
    END;
    $$ LANGUAGE plpgsql;
""")

    trigger_remover_prerequisito = _sql.DDL(
    """
    CREATE OR REPLACE TRIGGER remover_prerequisito
    BEFORE DELETE ON disciplina
    FOR EACH ROW
    EXECUTE FUNCTION remove_prerequisito();
"""
)

    function_remove_aluno_info = _sql.DDL(
    """
    CREATE OR REPLACE FUNCTION remove_aluno_info()
    RETURNS TRIGGER AS $$
    BEGIN
        DELETE FROM telefone t WHERE id_telefone = OLD.id_telefone;
        DELETE FROM endereco a WHERE id_endereco = OLD.id_endereco;
        DELETE FROM historico h WHERE id_historico = OLD.id_historico;
    END;
    $$ LANGUAGE plpgsql;
"""
)

    trigger_remover_aluno_info = _sql.DDL(
    """
    CREATE OR REPLACE TRIGGER remover_aluno_info
    BEFORE DELETE ON aluno
    FOR EACH ROW
    EXECUTE FUNCTION remove_aluno_info();
"""
)

    function_remove_professor_info = _sql.DDL(
    """
    CREATE OR REPLACE FUNCTION remove_professor_info()
    RETURNS TRIGGER AS $$
    BEGIN
        DELETE FROM telefone t WHERE id_telefone = OLD.id_telefone;
        DELETE FROM endereco a WHERE id_endereco = OLD.id_endereco;
        DELETE FROM historico h WHERE id_historico = OLD.id_historico;
    END;
    $$ LANGUAGE plpgsql;
"""
)

    trigger_remover_professor_info = _sql.DDL(
    """
    CREATE OR REPLACE TRIGGER remover_professor_info
    BEFORE DELETE ON professor
    FOR EACH ROW
    EXECUTE FUNCTION remove_professor_info();
"""
)


    with engine.connect() as conn:
        conn.execute(function_remove_prerequisito)
        conn.execute(trigger_remover_prerequisito)
        conn.commit()