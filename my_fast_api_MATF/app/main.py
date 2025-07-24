from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.customer import Customer
from app.models.cuenta import Cuenta
from app.routes import customers, cuentas

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API de productos con FastAPI y Oracle"}

app.include_router(customers.router)
app.include_router(cuentas.router)