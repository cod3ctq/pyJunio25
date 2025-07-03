from Actividad.Animal import Animal

class Acuaticos(Animal):
    def __init__(self,especie, raza, color, size, edad,transporte):
        super().__init__(especie, raza, color, size, edad)
        self._transporte = transporte

    @property
    def transporte(self):
        return self._transporte

    @transporte.setter
    def num_patas(self, valor):
        self._num_patas = valor

    # Puedes sobreescribir descripcion() para agregar num_patas
    def descripcion(self):
        # Llamar a descripcion() de Animal
        super().descripcion()
        # Mostrar info adicional
        print("Se transporta por Agua")
        print(f"El {self.especie} se transporta: {self.transporte}")