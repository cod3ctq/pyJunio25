from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#url de conexion a oracle
#FORMATO: oracle+oracledb:/usuario:contraseña@host:puerto/?service_name=XE
DATABASE_URL = "oracle+oracledb://db1:admin@localhost:1521/?service_name=XE"
#CREAR ENGINE SQLAchemy
engine = create_engine(DATABASE_URL)
#SESSION DE BASE DE DATOS
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
#base para los modelos orm
Base = declarative_base()