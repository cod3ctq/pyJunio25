from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.customer import Customer
from app.models.cuentas import Cuentas
from app.routers import customer
from app.routers import cuentas

app = FastAPI()
#Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API de customer con FastAPI y Oracle"}
#productos -->customer
app.include_router(customer.router)
app.include_router(cuentas.router)


