from ejercicioHerencia_AQR.Electronico import Electronico

class Celular(Electronico):
    def __init__(self, marca, precio, camara_mp):
        super().__init__(marca, precio)
        self._camara_mp = camara_mp

    def get_camara_mp(self):
        return self._camara_mp

    def set_camara_mp(self, camara_mp):
        self._camara_mp = camara_mp

    def __str__(self):
        base = super().__str__()
        return f"{base}, Cámara: {self._camara_mp} MP"

