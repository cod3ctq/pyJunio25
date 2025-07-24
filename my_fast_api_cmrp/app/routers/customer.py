from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.customer import CustomerCreate, CustomerRead
from app.db.database import SessionLocal
from app.services import customer_service

router = APIRouter(prefix="/customer", tags=["customer"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CustomerRead])
#@router.get("/", response_model=str)
def listar_customer(db: Session = Depends(get_db)):
    return customer_service.get_all_customer(db)
    #return 'hola'
@router.get("/{customer_id}", response_model=CustomerRead)
def obtener_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_service.get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer no encontrado")
    return customer

@router.post("/", response_model=CustomerRead)
def crear_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)

@router.delete("/{customer_id}")
def eliminar_customer(customer_id: int, db: Session = Depends(get_db)):
    ok = customer_service.delete_customer(db, customer_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Customer no encontrado")
    return {"ok": True}

@router.get("/buscar/", response_model=List[CustomerRead])
def buscar_por_nombre_y_precio(nombre: str, db: Session = Depends(get_db)):
    return customer_service.get_customer_by_name_and_price_range(db, nombre)
