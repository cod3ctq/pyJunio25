from fastapi import FastAPI
from routers import customers_proxy
from routers import cuentas_proxy

app = FastAPI(title="API Gateway - MATF")

app.include_router(customers_proxy.router)
app.include_router(cuentas_proxy.router)
@app.get("/")
def root():
    return {"message": "API Gateway funcionando correctamente"}