from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from typing import List
from app.cuentas_service.schemas.cuentas import CuentasCreate, CuentasRead
from app.cuentas_service.db.database import SessionLocal
from app.cuentas_service.crud import cuentas_service

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_model=List[CuentasRead])
#@router.get("/", response_model=str)
def listar_cuentas(db: Session = Depends(get_db)):
    return cuentas_service.get_all_cuentas(db)
    #return 'hola'
@app.get("/{cuenta_id}", response_model=CuentasRead)
def obtener_cuentas(cuentas_id: int, db: Session = Depends(get_db)):
    cuentas = cuentas_service.get_cuentas_by_id(db, cuentas_id)
    if not cuentas:
        raise HTTPException(status_code=404, detail="cuentas no encontrado")
    return cuentas

@app.post("/", response_model=CuentasRead)
def crear_cuentas(cuentas: CuentasCreate, db: Session = Depends(get_db)):
    return cuentas_service.create_cuentas(db, cuentas)

@app.delete("/{cuentas_id}")
def eliminar_cuentas(cuentas_id: int, db: Session = Depends(get_db)):
    ok = cuentas_service.delete_cuentas(db, cuentas_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Cuentas no encontrado")
    return {"ok": True}

@app.get("/buscar/", response_model=List[CuentasRead])
def buscar_por_nombre_y_precio(nombre: str, db: Session = Depends(get_db)):
    return cuentas_service.get_cuentas_by_name_and_price_range(db, nombre)
