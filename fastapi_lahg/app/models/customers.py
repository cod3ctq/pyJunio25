from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class Customer(Base):
    __tablename__ = "CUSTOMERS"

    cliente_id = Column("CLIENTE_ID", Integer, primary_key=True, index=True)
    nombre = Column("NOMBRE", String(100), nullable=False)
    direccion = Column("DIRECCION", String(200), nullable=False)
    curp = Column("CURP", String(18), nullable=False)
    fecha_nac = Column("FECHA_NAC", Date, nullable=False)

    cuentas = relationship("Cuenta", back_populates="cliente")

