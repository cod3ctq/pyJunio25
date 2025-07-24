from pydantic import BaseModel




# Para crear un departamento
class CuentaCreate(BaseModel):
    CLIENTE_ID: int
    NUM_CUENTA: int
    TIPO_CUENTA_ID: int
    SALDO: int
# Para leer un departamento
class CuentaRead(BaseModel):
    CUENTA_ID: int
    CLIENTE_ID: int
    NUM_CUENTA: int
    TIPO_CUENTA_ID: int
    SALDO: int


    class Config:
        orm_mode = True