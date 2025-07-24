from datetime import date
from typing import List

from pydantic import BaseModel

#para leer un cuenta
class CuentasRead(BaseModel):
    cuenta_id: int
    cliente_id: int
    num_cuenta: int
    tipo_cuenta_id: int
    saldo: int

    class Config:
        orm_mode = True

#para crear un cuenta
class CuentasCreate(BaseModel):
    nombre: str






