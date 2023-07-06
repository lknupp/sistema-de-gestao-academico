import fastapi as _fastapi
import src.database as _database
from src.routes import pessoaRouter as _pessoaRouter

app = _fastapi.FastAPI()

_database.create_database()

app.include_router(_pessoaRouter.router)