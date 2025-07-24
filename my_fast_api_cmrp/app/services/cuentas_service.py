from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.cuentas import Cuentas
from app.schemas.cuentas import CuentasCreate
from typing import List

def get_all_cuentas(db: Session) -> List[Cuentas]:
    return db.query(Cuentas).all()

def get_cuentas_by_id(db: Session, cuenta_id: int) -> Cuentas:
    return db.query(Cuentas).filter(Cuentas.cuenta_id == cuenta_id).first()

def create_cuentas(db: Session, cuentas: CuentasCreate) -> Cuentas:
    db_cuentas = Cuentas(**cuentas.dict())
    db.add(db_cuentas)
    db.commit()
    db.refresh(db_cuentas)
    return db_cuentas

def delete_cuentas(db: Session, cuenta_id: int) -> bool:
    cuentas = db.query(Cuentas).filter(Cuentas.cuenta_id == cuenta_id).first()
    if cuentas:
        db.delete(cuentas)
        db.commit()
        return True
    return False

def get_cuentas_by_name_and_price_range(db: Session, name: str) -> List[Cuentas]:
    return db.query(Cuentas).filter(
        Cuentas.nombre.contains(name),
    ).all()


