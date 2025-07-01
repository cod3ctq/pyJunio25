#ruta de lectura
import csv

ruta_lectura = "C:\\Users\\silve\\Downloads\\autos_aleatorios.csv"

autos = []

def leer_autos(ruta):
    with open(ruta, mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
        return autos

def filtrar_por_marca(ruta, campo, valor):
    resultados = []
    try:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            resultados = [fila for fila in lector if fila[campo] == valor]
        return resultados
    except Exception as e:
        return f"Error: {e}"

'''
#almacena todos los datos que ya fueron leídos
autos_leidos = leer_autos(ruta_lectura)
for auto in autos_leidos:
    print(auto)
'''

autos_filtrados = filtrar_por_marca(ruta_lectura, 'MARCA', 'Hyundai')
for auto in autos_filtrados:
    print(auto)


