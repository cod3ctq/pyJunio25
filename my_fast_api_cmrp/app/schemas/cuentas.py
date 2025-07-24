from pydantic import BaseModel

#para crear un cuenta
class CuentasCreate(BaseModel):
    nombre: str


#para leer un cuenta
class CuentasRead(BaseModel):
    cuenta_id: int
    cliente_id: int
    num_cuenta: int
    tipo_cuenta_id: int
    saldo: int

    class Config:
        orm_mode = True


