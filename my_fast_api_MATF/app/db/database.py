from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a Oracle
# Formato: oracle+oracledb://usuario:contraseña@host:puerto/?service_name=XE
DATABASE_URL = "oracle+oracledb://db1:admin@localhost:1521/?service_name=XE"
# Crear engine SQLAlchemy
engine = create_engine(DATABASE_URL)
# Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base para los modelos ORM
Base = declarative_base()