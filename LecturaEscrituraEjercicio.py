import csv

#Define una lista donde almacenaremos la info
def leer_autos(ruta):
    autos = []
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

def agregar_auto(ruta, auto):
    with open(ruta, mode='a+', newline='', encoding='utf8') as archivo_escritura:
        columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
        escritor = csv.DictWriter(archivo_escritura, columnas)
        escritor.writerow(auto)

def lista_hyundai(autos, ruta_salida):
    resultado = [auto for auto in autos if auto["MARCA"].strip().lower() == "hyundai"]
    guardar_autos(resultado, ruta_salida)

def lista_deportivos_rojos(autos, ruta_salida):
    resultado = [auto for auto in autos if auto["TIPO"].strip().lower() == "deportivo" and auto["COLOR"].strip().lower() == "rojo"]
    guardar_autos(resultado, ruta_salida)

def lista_autos_2000(autos, ruta_salida):
    resultado = [auto for auto in autos if int(auto["AÑO_LANZAMIENTO"]) > 2000]
    guardar_autos(resultado, ruta_salida)

def lista_promedio_precio_audi(autos, ruta_salida):
    audi_autos = [auto for auto in autos if auto["MARCA"].strip().lower() == "audi"]
    precios = [float(auto["PRECIO"]) for auto in audi_autos if auto["PRECIO"].replace('.', '', 1).isdigit()]
    promedio = sum(precios) / len(precios) if precios else 0

    with open(ruta_salida, mode='w', newline='', encoding='utf8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["MARCA", "PROMEDIO_PRECIO"])
        escritor.writerow(["Audi", f"{promedio:.2f}"])

def lista_electricos_familiares(autos, ruta_salida):
    resultado = [
        auto for auto in autos
        if auto["ELECTRICO"].strip().lower() == "true" and auto["TIPO"].strip().lower() == "familiar"
    ]
    guardar_autos(resultado, ruta_salida)

#Guarda una lista de autos en un archivo CSV
def guardar_autos(lista_autos, ruta_salida):
    if lista_autos:
        columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
        with open(ruta_salida, mode='w+', newline='', encoding='utf8') as archivo:
            escritor = csv.DictWriter(archivo, columnas)
            escritor.writeheader()
            for auto in lista_autos:
                escritor.writerow(auto)
        print(f"Archivo creado: {ruta_salida}")
    else:
        print(f"No se encontraron autos para guardar en {ruta_salida}")

#Ubicación del archivo que se leerá
ruta_lectura = "C:\\Users\\Alex Quijano\\Documents\\Python\\Ejercicios_LecturaEscritura2\\autos_aleatorios.csv"
autos_leidos = leer_autos(ruta_lectura)

#Imprime la lista completa
"""print("Todos los autos:")
for auto in autos_leidos:
    print(auto)
"""

auto_nuevo = {
    "MARCA": "Bocho",
    "MODELO": "El chido",
    "TIPO": "Familiar",
    "AÑO_LANZAMIENTO": "1950",
    "PRECIO": "333666",
    "COLOR": "Gris",
    "ELECTRICO": "True",
}
agregar_auto(ruta_lectura, auto_nuevo) #Llamada a la función que escribe dentro del csv

#Creación de los archivos CSV filtrados en la dirección indicada
lista_hyundai(autos_leidos, "C:\\Users\\Alex Quijano\\Documents\\Python\\Ejercicios_LecturaEscritura2\\autos_hyundai.csv")
lista_deportivos_rojos(autos_leidos, "C:\\Users\\Alex Quijano\\Documents\\Python\\Ejercicios_LecturaEscritura2\\autos_deportivos_rojos.csv")
lista_autos_2000(autos_leidos, "C:\\Users\\Alex Quijano\\Documents\\Python\\Ejercicios_LecturaEscritura2\\autos_modernos.csv")
lista_promedio_precio_audi(autos_leidos, "C:\\Users\\Alex Quijano\\Documents\\Python\\Ejercicios_LecturaEscritura2\\promedio_audi.csv")
lista_electricos_familiares(autos_leidos, "C:\\Users\\Alex Quijano\\Documents\\Python\\Ejercicios_LecturaEscritura2\\autos_electricos_familiares.csv")

