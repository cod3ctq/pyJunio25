from Actividad.Animal import Animal


class Animal_Acuatico(Animal):
    def __init__(self, especie, nombre, mar):
        super().__init__(especie, nombre)
        self.mar = mar
    @property
    def get_mar(self):
        return self.mar
    @get_mar.setter
    def get_mar(self, mar):
        self.mar = mar

    def andar(self):
        print(self.nombre+" su especie es "+self.especie+ " anda sobre el mar ", self.mar)
        print("Nada")