from prueba2.SeleccionFutbol import SeleccionFutbol

class   Futbolista(SeleccionFutbol):

    def __init__(self,nombre,apellido,edad,pocision,equipo):
        super().__init__(nombre, apellido,edad)
        self.pocision = pocision
        self.equipo = equipo

    def jugar_partido(self):
        print('jugar partido ')
        print(self.nombre,' --> ',self.apellido,'--> ')

    def concentrarse(self):
        print('sobre escribe metodo concentrarse ')
        print(self.nombre, ' --> ', self.apellido, '--> ', self.pocision, '--> ', self.equipo)