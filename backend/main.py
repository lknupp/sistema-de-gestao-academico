import fastapi as _fastapi
import src.database.database as _database
from src.routes import alunoRoute as _alunoRoute
from src.routes import enderecoRoute as _enderecoRoute
from src.routes import professorRoute as _profRoute
from src.routes import telefoneRoute as _telRoute
from src.routes import cursoRoute as _cursoRoute
from src.routes import disciplinaRoute as _disciplinaRoute
from src.routes import prerequisitoRoute as _prerequisitoRoute
from src.routes import campusRoute as _campusRoute
from src.routes import ofertaRoute as _ofertaRoute

description = "Sistema de gerenciamento que visa auxiliar o gerenciamento de uma unidade de ensino"
app = _fastapi.FastAPI(
    title="Sistema de Gestão Acadêmica", description=description, version="1.0.0"
)

_database.create_database()

app.include_router(_cursoRoute.router)
app.include_router(_disciplinaRoute.router)
app.include_router(_prerequisitoRoute.router)
app.include_router(_alunoRoute.router)
app.include_router(_profRoute.router)
app.include_router(_enderecoRoute.router)
app.include_router(_telRoute.router)
app.include_router(_campusRoute.router)
app.include_router(_ofertaRoute.router)

_database.create_function()
