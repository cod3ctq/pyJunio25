from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

MICROSERVICE_URL = "http://127.0.0.1:8002"

@app.get("/")
def root():
    return {"message": "API Gateway activo"}

@app.get("/customers")
async def get_customers():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{MICROSERVICE_URL}/customers/")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con el microservicio: {str(e)}")
@app.get("/cuentas")
async def get_cuentas():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{MICROSERVICE_URL}/cuentas/")
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error al conectar con el microservicio: {str(e)}")
