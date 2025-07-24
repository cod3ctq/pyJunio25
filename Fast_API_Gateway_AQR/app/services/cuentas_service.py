from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.customers import Customers
from app.schemas.customers import CustomersCreate
from typing import List
from app.exceptions.http_exceptions import (
    cliente_no_encontrado_exception,
    cliente_existente_exception,
    error_crear_cliente_exception,
    error_eliminar_cliente_exception
)

def get_all_customers(db: Session) -> list[type[Customers]]:
    return db.query(Customers).all()

def get_customer_by_id(db: Session, cliente_id: int) -> Customers:
    customer = db.query(Customers).filter(Customers.cliente_id == cliente_id).first()
    if not customer:
        raise cliente_no_encontrado_exception()
    return customer

def create_customers(db: Session, cliente: CustomersCreate) -> Customers:
    try:
        cliente_existente = db.query(Customers).filter(Customers.nombre == cliente.nombre).first()
        if cliente_existente:
            raise cliente_existente_exception()

        db_customers = Customers(**cliente.dict())
        db.add(db_customers)
        db.commit()
        db.refresh(db_customers)
        return db_customers
    except Exception:
        raise error_crear_cliente_exception()

def delete_customer_by_id(db: Session, cliente_id: int) -> Customers:
    cliente = db.query(Customers).filter(Customers.cliente_id == cliente_id).first()
    if not cliente:
        raise cliente_no_encontrado_exception()
    try:
        db_customers = get_customer_by_id(db, cliente_id)
        db.delete(db_customers)
        db.commit()
        return db_customers
    except Exception:
        raise error_eliminar_cliente_exception()

def update_customer_by_id(db: Session, cliente_id: int) -> Customers:
    db_customers = get_customer_by_id(db, cliente_id)
    db_customers.id = cliente_id
    db.commit()
    return db_customers






