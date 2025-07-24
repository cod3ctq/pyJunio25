from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# URL de conexió
# n a Oracle
# Formato: oracle+oracledb://usuario:contraseña@host:puerto/?service_name=XE
#EN ESTE CAOS YA ME PROPORCIONAN EL URL PORQUE CUENTA CON USUARIO, CONTRASEÑA HOST PUERTO ETC
DATABASE_URL = "oracle+oracledb://db1:admin@localhost:1521/?service_name=XE"
# Crear engine SQLAlchemy
engine = create_engine(DATABASE_URL)
# Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base para los modelos ORM
Base = declarative_base()




#DE ESTA MANERA SE PUEDE COMPROBAR SI LA CONEXIÓN CON LA BASE DE DATOS FUE EXITOSA
from sqlalchemy import text
from app.db.database import SessionLocal

def probar_conexion():
    try:
        db = SessionLocal()
        resultado = db.execute(text("SELECT 1 FROM DUAL"))
        print("✅ Conexión exitosa:", list(resultado))
    except Exception as e:
        print("❌ Error de conexión:", e)
    finally:
        db.close()

if __name__ == "__main__":
    probar_conexion()
