from Actividad.Animal import Animal


class Animal_Terrestre(Animal):
    def __init__(self, especie, nombre, territorio):
        super().__init__(especie, nombre)
        self.territorio = territorio

    @property
    def get_territorio(self):
        return self.territorio
    @get_territorio.setter
    def get_territorio(self, territorio):
        self.territorio = territorio

    def andar(self):
        print(self.nombre+" su especie es "+self.especie+" anda sobre la tierra en ", self.territorio)
        print("Camina")