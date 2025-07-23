from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate
from typing import List
from app.exceptios.http_exceptions import (
    customer_no_encontrado_exception,
    customer_existente_exception,
    error_crear_customer_exception,
    error_eliminar_customer_exception
)

def get_all_customer(db: Session) -> List[Customer]:
    return db.query(Customer).all()

def get_customer_by_id(db: Session, customer_id: int) -> Customer:
    customer = db.query(Customer).filter(Customer.CLIENTE_ID == customer_id).first()
    if not customer:
        raise customer_no_encontrado_exception()
    return customer

def create_customer(db: Session, customer: CustomerCreate) -> Customer:
    try:
        # Verificación opcional: evitar duplicados por nombre
        customer_existente = db.query(Customer).filter(Customer.NOMBRE == customer.NOMBRE).first()
        if customer_existente:
            raise customer_existente_exception()

        db_customer = Customer(**customer.dict())
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    except Exception:
        raise error_crear_customer_exception()
def delete_customer(db: Session, cliente_id: int) -> bool:
    customer = db.query(Customer).filter(Customer.CLIENTE_ID == cliente_id).first()
    if not customer:
        raise customer_no_encontrado_exception()
    try:
        db.delete(customer)
        db.commit()
        return True
    except Exception:
        raise error_eliminar_customer_exception()
"""
def get_productos_by_name_and_price_range(db: Session, name: str, min_price: float, max_price: float) -> List[Producto]:
    return db.query(Producto).filter(
        Producto.nombre.contains(name),
        Producto.precio_venta >= min_price,
        Producto.precio_venta <= max_price
    ).all()
"""