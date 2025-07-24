from fastapi import APIRouter, HTTPException
import httpx
from services.urls import CUSTOMERS_SERVICE_URL

router = APIRouter(prefix="/customers", tags=["Gateway - Customers"])

@router.get("/")
async def listar_customers():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMERS_SERVICE_URL}/customers/")
    return r.json()

@router.get("/{cliente_id}")
async def obtener_customer(cliente_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMERS_SERVICE_URL}/customers/{cliente_id}")
    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return r.json()

@router.post("/")
async def crear_customer_proxy(customer: dict):  # dict o CustomerCreate si quieres validación aquí también
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{CUSTOMERS_SERVICE_URL}/customers/",
            json=customer
        )
    return response.json()
@router.delete("/{cliente_id}")
async def eliminar_customer(cliente_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMERS_SERVICE_URL}/customers/{cliente_id}")
    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return r.json()