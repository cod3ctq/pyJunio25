from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

CUSTOMER_SERVICE = "http://localhost:8001"
CUENTAS_SERVICE = "http://localhost:8002"

@app.get("/customer")
async def proxy_customer():
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{CUSTOMER_SERVICE}/customer")
        return resp.json()
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Users service unavailable")

@app.get("/cuentas")
async def proxy_order():
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{CUENTAS_SERVICE}/cuentas")
        return resp.json()
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Orders service unavailable")