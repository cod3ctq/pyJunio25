from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

class Cuentas(Base):
    __tablename__ = "cuentas"

    cuenta_id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("customers.cliente_id"), nullable=False)
    num_cuenta = Column(Integer, nullable=False)
    tipo_cuenta_id = Column(String, nullable=False)
    saldo = Column(Integer, nullable=False)

    customer = relationship("Customers", backref="cuentas")
