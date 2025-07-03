class SeleccionFutbol:

    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def get_nombre(self):
        return self.nombre

    @get_nombre.setter
    def set_nombre(self, nombre):
        self.nombre = nombre

    @property
    def get_apellido(self):
        return self.apellido

    @get_apellido.setter
    def set_apellido(self,apellido):
        self.apellido = apellido

    @property
    def get_edad(self):
        return self.edad

    @get_edad.setter
    def set_edad(self,edad):
        self.edad = edad
    ####metodos---------->#####
    def viajar(self):
        print('ir de viaje')
        print(self.nombre)

    def concentrarse(self):
        print('ir a la concentrasion')
        print(self.nombre,' --> ',self.apellido)
