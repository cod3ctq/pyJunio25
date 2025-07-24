from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Cuentas(Base):
    __tablename__ = "cuentas"

    cuenta_id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("customer.cliente_id"), nullable=False)
    num_cuenta = Column(Integer, nullable=False)
    tipo_cuenta_id = Column(Integer, nullable=False)
    saldo = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="cuentas")
