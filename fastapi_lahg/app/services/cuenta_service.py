from sqlalchemy.orm import Session
from app.models.cuentas import Cuenta as CuentaModel
from app.schemas.cuentas import CuentaCreate
from typing import List
from sqlalchemy.orm import joinedload
from app.exceptions.http_exceptions import (
    cuenta_no_encontrada_exception,
    cuenta_existente_exception,
    error_crear_cuenta_exception,
    error_eliminar_cuenta_exception
)

def get_all_cuentas(db: Session) -> List[CuentaModel]:
    return db.query(CuentaModel).all()

def get_cuenta_by_id(db: Session, cuenta_id: int) -> CuentaModel:
    cuenta = db.query(CuentaModel).filter(CuentaModel.cuenta_id == cuenta_id).first()
    if not cuenta:
        raise cuenta_no_encontrada_exception()
    return cuenta

def create_cuenta(db: Session, cuenta: CuentaCreate) -> CuentaModel:
    try:
        # Opcional: verificar si num_cuenta ya existe para evitar duplicados
        cuenta_existente = db.query(CuentaModel).filter(CuentaModel.num_cuenta == cuenta.num_cuenta).first()
        if cuenta_existente:
            raise cuenta_existente_exception()

        db_cuenta = CuentaModel(**cuenta.dict())
        db.add(db_cuenta)
        db.commit()
        db.refresh(db_cuenta)
        return db_cuenta
    except Exception:
        raise error_crear_cuenta_exception()

def delete_cuenta(db: Session, cuenta_id: int) -> bool:
    cuenta = db.query(CuentaModel).filter(CuentaModel.cuenta_id == cuenta_id).first()
    if not cuenta:
        raise cuenta_no_encontrada_exception()
    try:
        db.delete(cuenta)
        db.commit()
        return True
    except Exception:
        raise error_eliminar_cuenta_exception()

#Join
def get_cuentas_con_clientes(db: Session) -> List[CuentaModel]:
    return db.query(CuentaModel).options(joinedload(CuentaModel.cliente)).all()
