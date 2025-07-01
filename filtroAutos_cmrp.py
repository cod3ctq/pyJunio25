import csv

ruta_lectura = "C:\\Users\\USUARIO\\Documents\\autos_aleatorios.csv"
ruta_escritura = "C:\\Users\\USUARIO\\Documents\\filtroAutosDeportivos.csv"


def autos_(ruta_lectura):
    autos = []
    with open(ruta_lectura,mode='r', newline='', encoding='utf8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            autos.append(fila)
    return autos

autos_leidos = autos_(ruta_lectura)
################
def agregar_auto(ruta_escritura,auto):
    with open(ruta_escritura, mode='a', newline='',encoding='utf8') as escritura:
        #define la estructura de  columnas para que elescritor la conozca
        columnas = ['MARCA','MODELO','TIPO','AÑO_LANZAMIENTO','PRECIO','COLOR','ELECTRICO']
        escritor = csv.DictWriter(escritura,columnas)
        escritor.writerow(auto)

################
def filtro_autos_deportivos(autos_leidos,ruta_escritura):

    for autos in autos_leidos:
        if autos['TIPO'] == 'Deportivo' and autos['COLOR'] == 'Rojo':
            print(autos)
            agregar_auto(ruta_escritura,autos)

################
def filtro_autos_anio(autos_leidos,ruta_escritura):
    for autos in autos_leidos:
        if int(autos['AÑO_LANZAMIENTO']) >= 2020:
            print(autos)
            agregar_auto(ruta_escritura, autos)

################
def filtro_autos_electrico_familiar(autos_leidos,ruta_escritura):
    for autos in autos_leidos:
        if autos['TIPO'] == 'Familiar' and autos['ELECTRICO'] == 'Sí':
            print(autos)
            agregar_auto(ruta_escritura, autos)

################
def filtro_auto_marca(autos_leidos):
    for autos in autos_leidos:
        if autos['MARCA'] == 'Hyundai':
            print(autos)
            agregar_auto(ruta_escritura, autos)

################

def agregar_auto_promedio(ruta_lectura,autos_leidos):
    with open(ruta_lectura, mode='a', newline='',encoding='utf8') as escritura:
        #define la estructura de  columnas para que elescritor la conozca
        columnas = ['MARCA','MODELO','TIPO','AÑO_LANZAMIENTO','PRECIO','COLOR','ELECTRICO','PROMEDIO']
        escritor = csv.DictWriter(escritura,columnas)
        escritor.writerow(autos_leidos)

def filtro_autos_promedio(autos_leidos,ruta_escritura):
    total=0
    contador=0
    for autos in autos_leidos:
        if autos['MARCA'] > 'AUDI':
            total = total + int(autos['PRECIO'])
            contador = +1
    for autos in autos_leidos:
        if autos['MARCA'] > 'AUDI':
            autos['PROMEDIO'] = total / contador
            agregar_auto_promedio(ruta_escritura, autos)
    print('promedio de marca audi: ', total / contador)

##################


opcion = int(input('(1)-->autos depo\n(2)-->autos año\n(3)-->autos electrico/familiar\n(4)-->autos marca\n(5)-->autos promedio:\n   '))

if opcion == 1:
    filtro_autos_deportivos(autos_leidos,ruta_escritura)
elif opcion == 2:
    filtro_autos_anio(ruta_lectura,ruta_escritura)
elif opcion == 3:
    filtro_autos_electrico_familiar(autos_leidos,ruta_lectura)
elif opcion == 4:
    filtro_auto_marca(autos_leidos)
elif opcion == 5:
    autos = filtro_autos_promedio(autos_leidos,ruta_escritura)
    agregar_auto_promedio(ruta_escritura, autos)

else:
    print('error')


