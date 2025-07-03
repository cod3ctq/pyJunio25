class Electronico:
    def __init__(self, marca, precio):
        self._marca = marca
        self._precio = precio

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"Marca: {self._marca}, Precio: ${self._precio:.2f}"

