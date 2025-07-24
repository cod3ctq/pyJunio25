
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Customer(Base):
    __tablename__ = "CUSTOMERS"

    CLIENTE_ID = Column(Integer, primary_key=True, index=True)
    NOMBRE = Column(String(255), nullable=False)
    DIRECCION = Column(String(255), nullable=False)
    CURP = Column(String(255), nullable=False)
    FECHA_NAC = Column(Date, nullable=False)

    cuentas = relationship("Cuenta", back_populates="cliente")
