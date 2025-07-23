from typing import List
from pydantic import BaseModel
from datetime import date



# Para crear un cliente
class CustomerCreate(BaseModel):
    nombre: str
    direccion: str
    curp: str
    fecha_nac: date  # Pydantic usará datetime.date

# Para leer un cliente completo (por ejemplo, en una consulta GET)
#Recuerda que la base de datos ya genera en automatico el cliente_id
class CustomerRead(CustomerCreate):
    cliente_id: int  # El ID se incluye solo en la respuesta
    cuentas: List["CuentaRead"] = []

    class Config:
        #from_attributes = True
        orm_mode = True

from app.schemas.cuentas import CuentaRead
CustomerRead.update_forward_refs()