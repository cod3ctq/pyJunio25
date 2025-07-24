from typing import List
from pydantic import BaseModel
from app.schemas.customers import CustomersRead


#Para crear una cuenta:
class CuentaCreate(BaseModel):
    num_cuenta: int
    tipo_cuenta_id: str
    saldo: int

#Para leer una cuenta:
class CuentaRead(BaseModel):
    cuenta_id: int
    cliente_id: List[CustomersRead] #Relacion cargada
    num_cuenta: int
    tipo_cuenta_id: str
    saldo: int
    class Config:
        orm_mode = True

