"""
Filtro para todos los autos de una marca elegida por el usuario
"""

import csv

def leer_autos(ruta):
    autos = []
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

def escribir_autos(ruta, autos_filtrados):
    columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
    with open(ruta, mode='x', newline='', encoding='utf8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        for auto in autos_filtrados:
            escritor.writerow(auto)

# Ubicacion del archivo que se leera
ruta_lectura = r"C:\Users\NITRO 5\Downloads\autos_aleatorios.csv"

# Almacena todos los datos que ya fueron leidos
autos_leidos = leer_autos(ruta_lectura)

# Pedir la marca al usuario
marca = input("¿Qué marca quieres buscar? ")

# Filtra los autos de esa marca
autos_filtrados = [auto for auto in autos_leidos if auto["MARCA"].lower() == marca.lower()]

# Muestra los autos filtrados
for auto in autos_filtrados:
    print(auto)

# Si se encontraron autos, los guarda
if autos_filtrados:
    # Nombre del nuevo archivo
    ruta_salida = rf"C:\Users\NITRO 5\Downloads\autos_{marca}.csv"
    try:
        escribir_autos(ruta_salida, autos_filtrados)
        print(f"Archivo creado correctamente: {ruta_salida}")
    except FileExistsError:
        print("ERROR: El archivo ya existe.")
else:
    print(f"No se encontraron autos de la marca {marca}.")


"""
Autos tipo deportivo y de color rojo
"""

import csv

def leer_autos(ruta):
    autos = []
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

def escribir_autos(ruta, autos_filtrados):
    columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
    with open(ruta, mode='x', newline='', encoding='utf8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        for auto in autos_filtrados:
            escritor.writerow(auto)

# Ubicacion del archivo que se leera
ruta_lectura = r"C:\Users\NITRO 5\Downloads\autos_aleatorios.csv"

# Almacena todos los datos que ya fueron leidos
autos_leidos = leer_autos(ruta_lectura)

# Pedir el al usuario y el color
tipo = input("¿Qué tipo de auto quieres buscar? ")
color = input("¿Qué color de auto quieres buscar?")


# Filtra los autos de ese tipo y color
autos_filtrados = [auto for auto in autos_leidos if auto["TIPO"].lower() == tipo.lower()]
autos_filtrados = [auto for auto in autos_filtrados if auto["COLOR"].lower() == color.lower()]


# Muestra los autos filtrados
for auto in autos_filtrados:
    print(auto)

# Si se encontraron autos, los guarda
if autos_filtrados:
    # Nombre del nuevo archivo
    ruta_salida = rf"C:\Users\NITRO 5\Downloads\autos_{tipo}_{color}.csv"
    try:
        escribir_autos(ruta_salida, autos_filtrados)
        print(f"Archivo creado correctamente: {ruta_salida}")
    except FileExistsError:
        print("ERROR: El archivo ya existe.")
else:
    print(f"No se encontraron autos de tipo {tipo} y color {color}.")

""""

3. Autos con año lanzamiento mayor a 2020

"""

"""
Filtro para todos los autos de una marca elegida por el usuario
"""

import csv

def leer_autos(ruta):
    autos = []
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

def escribir_autos(ruta, autos_filtrados):
    columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
    with open(ruta, mode='x', newline='', encoding='utf8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        for auto in autos_filtrados:
            escritor.writerow(auto)

# Ubicacion del archivo que se leera
ruta_lectura = r"C:\Users\NITRO 5\Downloads\autos_aleatorios.csv"

# Almacena todos los datos que ya fueron leidos
autos_leidos = leer_autos(ruta_lectura)

# Pedir la marca al usuario
lanzamiento = int(input("¿A partir de que año de lanzamiento quieres buscar? "))



# Filtra los autos de esa marca
autos_filtrados = [auto for auto in autos_leidos if int(auto["AÑO_LANZAMIENTO"]) >= lanzamiento]

# Muestra los autos filtrados
for auto in autos_filtrados:
    print(auto)

# Si se encontraron autos, los guarda
if autos_filtrados:
    # Nombre del nuevo archivo
    ruta_salida = rf"C:\Users\NITRO 5\Downloads\autos_{lanzamiento}.csv"
    try:
        escribir_autos(ruta_salida, autos_filtrados)
        print(f"Archivo creado correctamente: {ruta_salida}")
    except FileExistsError:
        print("ERROR: El archivo ya existe.")
else:
    print(f"No se encontraron autos de la marca {lanzamiento}.")

"""
4. Promedio de precio de los autos de la marca Audi
"""

import csv

def leer_autos(ruta):
    autos = []
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

def escribir_autos(ruta, autos_filtrados):
    columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
    with open(ruta, mode='x', newline='', encoding='utf8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        for auto in autos_filtrados:
            escritor.writerow(auto)

# Ubicacion del archivo que se leera
ruta_lectura = r"C:\Users\NITRO 5\Downloads\autos_aleatorios.csv"

# Almacena todos los datos que ya fueron leidos
autos_leidos = leer_autos(ruta_lectura)

# Pedir la marca al usuario
marca = input("¿Qué marca quieres buscar? ")

# Filtra los autos de esa marca
autos_filtrados = [auto for auto in autos_leidos if auto["MARCA"].lower() == marca.lower()]

# Muestra los autos filtrados
for auto in autos_filtrados:
    print(auto)

if autos_filtrados:
    precios = [int(auto["PRECIO"]) for auto in autos_filtrados]
    suma_precios = sum(precios)
    cantidad = len(precios)
    promedio = suma_precios / cantidad
    print(f"\nCantidad de autos encontrados: {cantidad}")
    print(f"Promedio de precio: ${promedio:.2f}")


# Si se encontraron autos, los guarda
if autos_filtrados:
    # Nombre del nuevo archivo
    ruta_salida = rf"C:\Users\NITRO 5\Downloads\autos_promedio de autos {marca}.csv"
    try:
        escribir_autos(ruta_salida, autos_filtrados)
        print(f"Archivo creado correctamente: {ruta_salida}")
    except FileExistsError:
        print("ERROR: El archivo ya existe.")
else:
    print(f"No se encontraron autos de la marca {marca}.")


"""
5. Autos Electricos y tipo familiar
"""

import csv

def leer_autos(ruta):
    autos = []
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

def escribir_autos(ruta, autos_filtrados):
    columnas = ["MARCA", "MODELO", "TIPO", "AÑO_LANZAMIENTO", "PRECIO", "COLOR", "ELECTRICO"]
    with open(ruta, mode='x', newline='', encoding='utf8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        for auto in autos_filtrados:
            escritor.writerow(auto)

# Ubicacion del archivo que se leera
ruta_lectura = r"C:\Users\NITRO 5\Downloads\autos_aleatorios.csv"

# Almacena todos los datos que ya fueron leidos
autos_leidos = leer_autos(ruta_lectura)

# Pedir el al usuario y el color
tipo = input("¿Qué tipo de auto quieres buscar? ")


# Filtra los autos de ese tipo y color
autos_filtrados = [auto for auto in autos_leidos if auto["TIPO"].lower() == tipo.lower()]
autos_filtrados = [auto for auto in autos_filtrados if auto["ELECTRICO"] == "Sí"]


# Muestra los autos filtrados
for auto in autos_filtrados:
    print(auto)

# Si se encontraron autos, los guarda
if autos_filtrados:
    # Nombre del nuevo archivo
    ruta_salida = rf"C:\Users\NITRO 5\Downloads\autos_{tipo}_eletrico.csv"
    try:
        escribir_autos(ruta_salida, autos_filtrados)
        print(f"Archivo creado correctamente: {ruta_salida}")
    except FileExistsError:
        print("ERROR: El archivo ya existe.")
else:
    print(f"No se encontraron autos de tipo {tipo} y electrico.")
