from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Cuenta(Base):
    __tablename__ = "CUENTAS"

    cuenta_id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("CUSTOMERS.CLIENTE_ID"), nullable=False)
    num_cuenta = Column(Integer, nullable=False)
    tipo_cuenta_id = Column(Integer, nullable=False)
    saldo = Column(Float, nullable=False)

    cliente = relationship("Customer", back_populates="cuentas")
