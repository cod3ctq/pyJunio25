from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.cuenta import CuentaCreate, CuentaRead
from app.db.database import SessionLocal
from app.services import cuenta_service

router = APIRouter(prefix="/cuentas", tags=["cuentas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CuentaRead])
def listar_cuenta(db: Session = Depends(get_db)):
    return cuenta_service.get_all_cuenta(db)

@router.get("/{cuenta_id}", response_model=CuentaRead)
def obtener_cuenta(cuenta_id: int, db: Session = Depends(get_db)):
    cuenta = cuenta_service.get_cuenta_by_id(db, cuenta_id)
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return cuenta

@router.post("/", response_model=CuentaRead)
def crear_cuenta(cuenta: CuentaCreate, db: Session = Depends(get_db)):
    return cuenta_service.create_cuenta(db, cuenta)

@router.delete("/{cuenta_id}")
def eliminar_cuenta(cuenta_id: int, db: Session = Depends(get_db)):
    ok = cuenta_service.delete_cuenta(db, cuenta_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return {"ok": True}