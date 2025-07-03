

class Empleado:
    def __init__(self, nombre, nss,dias_vacaciones, salario_base):
        self.nombre = nombre
        self.nss = nss
        self.dias_vacaciones = dias_vacaciones
        self.salario_base = salario_base

    @property
    def get_nombre(self):
        return self.nombre

    @property
    def get_nss(self):
        return self.nss

    @property
    def get_dias_vacaciones(self):
        return self.dias_vacaciones

    @property
    def get_salario_base(self):
        return self.salario_base

    @get_nombre.setter
    def set_nombre(self,nombre):
        self.nombre = nombre


    def checar_entrada(self):
        print(self.nombre,"ha llegó")

    def checar_salida(self):
        print(self.nombre,"ha salido")


