from fastapi import FastAPI
from app.db.database import engine, Base
#from app.db.database import Base, engine
from app.models.cuentas import Cuentas
from app.models.customers import Customers
from app.routers import cuentas

app = FastAPI(title="Fast API")
#Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API de Clientes con Fast API y Oracle"}

app.include_router(cuentas.router)