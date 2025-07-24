from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.cuentas import CuentaCreate, CuentaRead
from app.db.database import SessionLocal
from app.services import cuenta_service


router = APIRouter(prefix="/cuentas", tags=["cuentas"])

# Dependency para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CuentaRead])
def listar_productos(db: Session = Depends(get_db)):
    return cuenta_service.get_all_cuentas(db)

@router.get("/{cuenta_id}", response_model=CuentaRead)
def obtener_producto(cuenta_id: int, db: Session = Depends(get_db)):
    cuenta = cuenta_service.get_cuenta_by_id(db, cuenta_id)
    if not cuenta:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return cuenta

@router.post("/", response_model=CuentaRead)
def crear_producto(cuenta: CuentaCreate, db: Session = Depends(get_db)):
    try:
        return cuenta_service.create_cuenta(db, cuenta)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{cuenta_id}")
def eliminar_producto(cuenta_id: int, db: Session = Depends(get_db)):
    try:
        ok = cuenta_service.delete_cuenta(db, cuenta_id)
        if not ok:
            raise HTTPException(status_code=404, detail="Cuenta no encontrada")
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/con-clientes", response_model=List[CuentaRead])
def obtener_cuentas_con_clientes(db: Session = Depends(get_db)):
    return cuenta_service.get_cuentas_con_clientes(db)

