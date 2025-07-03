from ejercicioHerencia_AQR.Electronico import Electronico

class Laptop(Electronico):
    def __init__(self, marca, precio, ram_gb):
        super().__init__(marca, precio)
        self._ram_gb = ram_gb

    def get_ram_gb(self):
        return self._ram_gb

    def set_ram_gb(self, ram_gb):
        self._ram_gb = ram_gb

    def __str__(self):
        base = super().__str__()
        return f"{base}, RAM: {self._ram_gb} GB"