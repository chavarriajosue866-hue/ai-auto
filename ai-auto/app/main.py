from fastapi import FastAPI
from app.core.database import engine, Base
import app.models.models  # Importamos para que SQLAlchemy registre las tablas
from app.api import routes

# Usamos 'api_app' para que no choque con el nombre de la carpeta 'app'
api_app = FastAPI(title="AI Automation Core")

@api_app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@api_app.get("/")
def read_root():
    return {"status": "online", "message": "Cerebro listo para recibir órdenes"}

api_app.include_router(routes.router, prefix="/api")