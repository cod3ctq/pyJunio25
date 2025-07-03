class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre
    @property
    def get_especie(self):
        return self.especie
    @get_especie.setter
    def get_especie(self, especie):
        self.especie = especie
    @property
    def get_nombre(self):
        return self.nombre
    @get_nombre.setter
    def get_nombre(self, nombre):
        self.nombre = nombre

    def andar(self):
        print(self.nombre+" su especie es "+self.especie+" puede andar por tierra o mar")