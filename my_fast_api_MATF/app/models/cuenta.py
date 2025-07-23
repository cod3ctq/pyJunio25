from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

class Cuenta(Base):
    __tablename__ = "CUENTAS"

    CUENTA_ID = Column(Integer, primary_key=True, index=True)
    CLIENTE_ID = Column(Integer, ForeignKey("CUSTOMERS.CLIENTE_ID"), nullable=False)
    NUM_CUENTA = Column(Integer, nullable=False)
    TIPO_CUENTA_ID = Column(Integer, nullable=False)
    SALDO = Column(Integer, nullable=False)

    cliente = relationship("Customer", back_populates="cuentas")