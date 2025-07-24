from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from typing import List
from app.customer_service.schemas.customer import CustomerCreate, CustomerRead
from app.customer_service.db.database import SessionLocal
from app.customer_service.crud import customer_service

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_model=List[CustomerRead])
def listar_customer(db: Session = Depends(get_db)):
    return customer_service.get_all_customer(db)

@app.get("/{cliente_id}", response_model=CustomerRead)
def obtener_customer(cliente_id: int, db: Session = Depends(get_db)):
    customer = customer_service.get_customer_by_id(db, cliente_id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer no encontrado")
    return customer

@app.post("/", response_model=CustomerRead)
def crear_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)

@app.delete("/{cliente_id}")
def eliminar_customer(cliente_id: int, db: Session = Depends(get_db)):
    ok = customer_service.delete_customer(db, cliente_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Customer no encontrado")
    return {"ok": True}

@app.get("/buscar/", response_model=List[CustomerRead])
def buscar_por_nombre_y_precio(nombre: str, db: Session = Depends(get_db)):
    return customer_service.get_customer_by_name_and_price_range(db, nombre)




