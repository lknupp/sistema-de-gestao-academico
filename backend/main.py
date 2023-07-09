import fastapi as _fastapi
import src.database.sqlite as _database
from src.routes import alunoRoute as _alunoRoute
from src.routes import enderecoRoute as _enderecoRoute
<<<<<<< HEAD
from src.routes import professorRoute as _profRoute
from src.routes import telefoneRoute as _telRoute
=======
from src.routes import cursoRoute as _cursoRoute
>>>>>>> 9b9777e (feat: include cursoRoute to app.router)

app = _fastapi.FastAPI()

_database.create_database()

app.include_router(_alunoRoute.router)
app.include_router(_profRoute.router)
app.include_router(_enderecoRoute.router)
<<<<<<< HEAD
app.include_router(_telRoute.router)
=======
app.include_router(_cursoRoute.router)
>>>>>>> 9b9777e (feat: include cursoRoute to app.router)
