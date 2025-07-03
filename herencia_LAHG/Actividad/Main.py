from Actividad.Animal import Animal
from Actividad.Terrestres import Terrestre
from Actividad.Acuaticos import Acuaticos


class Main:

    animal1 = Animal("Perro","Chihuahua","Negro","Pequeño", 10)

    animal1.hacer_sonido("ladrido fuerte")
    animal1.moverse("cuatro patas")
    animal1.descripcion()

mi_terrestre = Terrestre(
    especie="Perro",
    raza="Pastor Alemán",
    color="Negro y café",
    size="Grande",
    edad=5,
    transporte="por tierra"
)

mi_acuatico = Acuaticos(
    especie="Pez",
    raza="Beta",
    color="Rojo",
    size="Pequeño",
    edad=1,
    transporte="por agua"
)

mi_terrestre.descripcion()
mi_terrestre.hacer_sonido("guau guau")


mi_acuatico.descripcion()
mi_acuatico.hacer_sonido("glu glu")
# Salida: El Perro hace 'guau guau'






