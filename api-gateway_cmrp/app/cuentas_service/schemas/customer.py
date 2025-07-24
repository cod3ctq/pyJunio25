from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from app.customer_service.schemas.cuentas import CuentasRead

# Para crear un customer
class CustomerCreate(BaseModel):
    nombre: str
    direccion: str
    curp: str
    fecha_nac: date

# Para leer un customer
class CustomerRead(BaseModel):
    cliente_id: int
    nombre: str
    direccion: str
    curp: str
    fecha_nac: date
    cuentas: List[CuentasRead]  # Relación cargada

    class Config:
        orm_mode = True
