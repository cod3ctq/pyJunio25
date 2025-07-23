from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.cuentas import Cuenta
from app.models.customers import Customer
from app.routers import cuentas  # asumiendo que tu router está en app/routers/cuentas.py

app = FastAPI()

# Crea las tablas si no existen
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API de cuentas y clientes con FastAPI y Oracle"}

# Incluye el router de cuentas
app.include_router(cuentas.router)
