from fastapi import APIRouter, HTTPException
import httpx
from services.urls import CUSTOMERS_SERVICE_URL

router = APIRouter(prefix="/cuentas", tags=["Gateway - Cuentas"])

@router.get("/")
async def listar_cuentas():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMERS_SERVICE_URL}/cuentas/")
    return r.json()

@router.get("/{cuentas_id}")
async def obtener_cuentas(cuentas_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMERS_SERVICE_URL}/cuentas/{cuentas_id}")
    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return r.json()
@router.post("/")
async def crear_cuenta_proxy(cuenta: dict):  # dict o CustomerCreate si quieres validación aquí también
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{CUSTOMERS_SERVICE_URL}/cuentas/",
            json=cuenta
        )
    return response.json()
@router.delete("/{cuenta_id}")
async def eliminar_cuenta(cuenta_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMERS_SERVICE_URL}/cuentas/{cuenta_id}")
    if r.status_code == 404:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return r.json()