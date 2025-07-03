class Animal:
    def __init__(self, especie, raza, color, size, edad):
        self._especie = especie
        self._raza = raza
        self._color = color
        self._size = size
        self._edad = edad

    # --- Propiedad: tipo --- get- me da el valor a  mi, y set- le da el valor al objeto
    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self,especie):
        self._especie = especie

    # --- Propiedad: raza ---
    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, raza):
        self._raza = raza

    # --- Propiedad: color ---
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    # --- Propiedad: size ---
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


    # --- Métodos adicionales ---
    def hacer_sonido(self, sonido):
        print(f"El {self.especie} hace '{sonido}'")

    def moverse(self, modo):
        print(f"El {self.especie} se mueve en {modo}")

    def descripcion(self):
        print(f"Especie: {self.especie}, Raza: {self.raza}, Color: {self.color}, Tamaño: {self.size}, Edad: {self.edad} años")

