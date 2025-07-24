from pydantic import BaseModel

from app.schemas.customers import CustomerRead


class CuentaCreate(BaseModel):
    cliente_id: int
    num_cuenta: int
    tipo_cuenta_id: int
    saldo: float


class CuentaRead(CuentaCreate):
    cuenta_id: int
    cliente: CustomerRead

    class Config:
        orm_mode = True
