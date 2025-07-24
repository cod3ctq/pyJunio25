from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL de conexión a Oracle
#Formato:
DATABASE_URL = "oracle+oracledb://db1:admin@localhost:1521/?service_name=XE"

#Crea engine SQLALchemy:
engine = create_engine(DATABASE_URL)

#Sesión a base de datos:
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para los modelos ORM:
Base = declarative_base()
