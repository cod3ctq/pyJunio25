from prueba2.SeleccionFutbol import SeleccionFutbol
from prueba2.Entrenador import Entrenador
from  prueba2.Futbolista import Futbolista

class Main:
    print('****************deportista')
    deportista = SeleccionFutbol('Juan', 'Perez', 100)
    deportista.viajar()
    deportista.concentrarse()
    print('****************jugador')
    jugador = Futbolista('pavel', 'pardo', 30,'medio','america')
    jugador.set_nombre = 'Rafael'
    jugador.set_apellido ='Marquez'
    jugador.set_edad = 25
    jugador.viajar()
    jugador.concentrarse()
    jugador.jugar_partido()
    print('****************entrenador')
    entrenador = Entrenador('pavel', 'pardo', 50,'mx')
    entrenador.viajar()
    entrenador.concentrarse()
    entrenador.dirigir_entrenamiento()