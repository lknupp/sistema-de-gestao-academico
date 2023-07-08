import fastapi as _fastapi
import src.database.sqlite as _database
from src.routes import alunoRoute as _alunoRoute
from src.routes import enderecoRoute as _enderecoRoute

app = _fastapi.FastAPI()

_database.create_database()

app.include_router(_alunoRoute.router)
app.include_router(_enderecoRoute.router)
