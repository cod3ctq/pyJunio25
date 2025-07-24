from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.customers import CustomersCreate, CustomersRead
from app.db.database import SessionLocal
from app.services import cuentas_service

router = APIRouter(prefix="/cuentas", tags=["cuentas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CustomersRead])
def listar_customers(db: Session = Depends(get_db)):
    return cuentas_service.get_all_customers(db)

@router.get("/{cliente_id}", response_model=CustomersRead)
def obtener_customer(cliente_id: int, db: Session = Depends(get_db)):
    return cuentas_service.get_customer_by_id(db, cliente_id)

@router.post("/", response_model=CustomersCreate)
def crear_customer(customer: CustomersCreate, db: Session = Depends(get_db)):
    return cuentas_service.create_customers(db, customer)

@router.delete("/{cliente_id}", response_model=CustomersRead)
def eliminar_customer(cliente_id: int, db: Session = Depends(get_db)):
    ok = cuentas_service.delete_customer_by_id(db, cliente_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cuentas_service.delete_customer_by_id(db, cliente_id)

@router.get("/buscar", response_model=List[CustomersRead])
def buscar_customers(db: Session = Depends(get_db)):
    return cuentas_service.get_all_customers(db)

