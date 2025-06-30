import  csv

#Define una lista donde almacenaremos la info
def leer_auto(ruta):
    autos = []

    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

def filtrar_marca(autos, ruta):
    for auto in autos:
        ruta_marca = ruta+"\\Marca.txt"
        if (auto["MARCA"] == "Hyundai"):
            with open(ruta_marca, mode='a', newline='', encoding='utf8') as escritura:
                #Define la estructura de columnas para que el escritor la conozca
                columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
                escritor = csv.DictWriter(escritura, columnas)
                escritor.writerow(auto)
    print("El proceso de filtro de la marca se ejecutó con exito")

def filtrar_tipo_color(autos, ruta):
    for auto in autos:
        ruta_marca = ruta+"\\Tipo_Color.txt"
        if (auto["TIPO"] == "Deportivo" and auto["COLOR"] == "Rojo"):
            with open(ruta_marca, mode='a', newline='', encoding='utf8') as escritura:
                #Define la estructura de columnas para que el escritor la conozca
                columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
                escritor = csv.DictWriter(escritura, columnas)
                escritor.writerow(auto)
    print("El proceso del filtro del tipo de color se ejecutó con exito")

def filtrar_anio_lanzamiento(autos, ruta):
    for auto in autos:
        ruta_marca = ruta+"\\Año_Lanzamiento.txt"
        if (auto["AÑO_LANZAMIENTO"] == "2020"):
            with open(ruta_marca, mode='a', newline='', encoding='utf8') as escritura:
                #Define la estructura de columnas para que el escritor la conozca
                columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
                escritor = csv.DictWriter(escritura, columnas)
                escritor.writerow(auto)
    print("El proceso del filtro del año de lanzamiento se ejecutó con exito")

def filtrar_promedio_audi(autos, ruta):
    contador = 0
    suma_precio = 0.0
    total_promedio = 0
    for auto in autos:
        ruta_marca = ruta+"\\Promedio_Audi.txt"
        if (auto["MARCA"] == "Audi"):
            contador += 1
            suma_precio += float(auto["PRECIO"])
    total_promedio = suma_precio / contador
    promedio = {"PROMEDIO": round(total_promedio,2)}
    with open(ruta_marca, mode='a', newline='', encoding='utf8') as escritura:
        # Define la estructura de columnas para que el escritor la conozca
        columnas = ["PROMEDIO"]
        escritor = csv.DictWriter(escritura, columnas)
        escritor.writerow(promedio)
    print("El proceso del filtro del promedio del precio de los audi se ejecutó con exito")

def filtrar_electricos_familiar(autos, ruta):
    for auto in autos:
        ruta_marca = ruta+"\\Electrico_Familiar.txt"
        if (auto["ELECTRICO"] == "Sí" and auto["TIPO"] == "Familiar"):
            with open(ruta_marca, mode='a', newline='', encoding='utf8') as escritura:
                #Define la estructura de columnas para que el escritor la conozca
                columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
                escritor = csv.DictWriter(escritura, columnas)
                escritor.writerow(auto)
    print("El proceso del filtro de los autos eléctricos familiar se ejecutó con exito")

#Ubicación del archivo que se leerá
ruta_lectura = "C:\\Users\\OctoPC\\Downloads\\Telegram Desktop\\autos_aleatorios.csv"
ruta_escritura = "C:\\Users\\OctoPC\\Downloads\\Ejercicios"
#almacena todos los datos que ya fueron leidos

autos_leidos = leer_auto(ruta_lectura)

filtrar_marca(autos_leidos, ruta_escritura)

filtrar_tipo_color(autos_leidos, ruta_escritura)

filtrar_anio_lanzamiento(autos_leidos, ruta_escritura)

filtrar_promedio_audi(autos_leidos, ruta_escritura)

filtrar_electricos_familiar(autos_leidos, ruta_escritura)