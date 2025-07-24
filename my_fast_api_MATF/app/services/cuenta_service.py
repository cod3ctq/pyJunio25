from sqlalchemy.orm import Session
from app.models.cuenta import Cuenta
from app.schemas.cuenta import CuentaCreate
from typing import List
from app.exceptios.http_exceptions import (
    cuenta_no_encontrada_exception,
    cuenta_existente_exception,
    error_crear_cuenta_exception,
    error_eliminar_cuenta_exception
)

def get_all_cuenta(db: Session) -> List[Cuenta]:
    return db.query(Cuenta).all()

def get_cuenta_by_id(db: Session, cuenta_id: int) -> Cuenta:
    cuenta = db.query(Cuenta).filter(Cuenta.CUENTA_ID == cuenta_id).first()
    if not cuenta:
        raise cuenta_no_encontrada_exception()
    return cuenta

def create_cuenta(db: Session, cuenta: CuentaCreate) -> Cuenta:
    #try:
        # Verificación opcional: evitar duplicados por nombre
    cuenta_existente = db.query(Cuenta).filter(Cuenta.NUM_CUENTA == cuenta.NUM_CUENTA).first()
    if cuenta_existente:
        raise cuenta_existente_exception()

    db_cuenta = Cuenta(**cuenta.dict())
    db.add(db_cuenta)
    db.commit()
    db.refresh(db_cuenta)
    return db_cuenta
    #except Exception:
        #raise error_crear_customer_exception()
def delete_cuenta(db: Session, cuenta_id: int) -> bool:
    cuenta = db.query(Cuenta).filter(Cuenta.CUENTA_ID == cuenta_id).first()
    if not cuenta:
        raise cuenta_no_encontrada_exception()
    try:
        db.delete(cuenta)
        db.commit()
        return True
    except Exception:
        raise error_eliminar_cuenta_exception()