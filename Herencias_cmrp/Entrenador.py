from prueba2.SeleccionFutbol import SeleccionFutbol

class Entrenador(SeleccionFutbol):

    def __init__(self,nombre,apellido,edad,federacion):
        super().__init__(nombre, apellido,edad)
        self.federacion = federacion


    def dirigir_entrenamiento(self):
        print('dirigiendo entrenamiento ')
        print(self.nombre)

    def viajar(self):
        print('el entrenador debe viajar antes que los jugadores')
        print(self.nombre,'---> ', self.apellido)
