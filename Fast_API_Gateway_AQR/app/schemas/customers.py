from pydantic import BaseModel
from datetime import date
from typing import Optional

class CustomersCreate(BaseModel):
    nombre: str
    direccion: str
    curp: str
    fecha_nac: date

class CustomersRead(BaseModel):
    cliente_id: int
    nombre: str
    direccion: str
    curp: str
    fecha_nac: Optional[date]
    class Config:
        orm_mode = True
