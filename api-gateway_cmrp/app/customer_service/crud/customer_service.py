from sqlalchemy.orm import Session
from app.customer_service.models.customer_cuentas import Customer
from app.customer_service.schemas.customer import CustomerCreate
from typing import List

def get_all_customer(db: Session) -> List[Customer]:
    return db.query(Customer).all()

def get_customer_by_id(db: Session, cliente_id: int) -> Customer:
    return db.query(Customer).filter(Customer.cliente_id == cliente_id).first()

def create_customer(db: Session, customer: CustomerCreate) -> Customer:
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, cliente_id: int) -> bool:
    customer = db.query(Customer).filter(Customer.cliente_id == cliente_id).first()
    if customer:
        db.delete(customer)
        db.commit()
        return True
    return False

def get_customer_by_name_and_price_range(db: Session, name: str) -> List[Customer]:
    return db.query(Customer).filter(
        Customer.nombre.contains(name),
    ).all()


