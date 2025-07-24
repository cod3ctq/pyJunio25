from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Customer(Base):
    __tablename__ = "customer"

    cliente_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    curp = Column(String(255), nullable=False)
    fecha_nac = Column(Date, nullable=False)

    cuentas = relationship("Cuentas", back_populates="customer")
