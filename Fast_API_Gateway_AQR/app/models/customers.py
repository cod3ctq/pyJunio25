from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class Customers(Base):
    __tablename__ = "customers"

    cliente_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    direccion = Column(String(255), nullable=False)
    curp = Column(String(255), nullable=False)
    fecha_nac = Column(Date, nullable=False)

    customer = relationship("Cuentas", backref="customers")
