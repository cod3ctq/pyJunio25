from datetime import date
from typing import List

from pydantic import BaseModel

from app.schemas.cuenta import CuentaRead


# Para crear un producto
class CustomerCreate(BaseModel):
    NOMBRE: str
    DIRECCION: str
    CURP: str
    FECHA_NAC: date

# Para leer un producto
class CustomerRead(BaseModel):
    CLIENTE_ID: int
    NOMBRE: str
    DIRECCION: str
    CURP: str
    FECHA_NAC: date
    cuentas : List[CuentaRead]
    class Config:
        orm_mode = True