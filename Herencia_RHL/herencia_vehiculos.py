class Vehiculo:
    def __init__(self, marca, modelo, year):
        self._marca = marca
        self._modelo = modelo
        self.__year = year

    #obtener el año
    @property
    def year(self):
        return self.__year

    #asignar validación del año
    @year.setter
    def year(self, new_year):
        self.__year = new_year

    def mostrar_info(self):
        print(f'Vehículo: {self._marca} | Modelo: {self._modelo} | Año: {self.__year} ')

class Coche(Vehiculo):
    def __init__(self, marca, modelo, year, puertas):
        super().__init__(marca, modelo, year)
        self.puertas = puertas

    def mostrar_info(self):
        print(f"Coche: {self._marca} {self._modelo}, {self.puertas} puertas, Año: {self.year}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, year, tipo):
        super().__init__(marca, modelo, year)
        self._tipo = tipo

    def mostrar_info(self):
        print(f"Moto: {self._marca} {self._modelo}, Tipo: {self._tipo}, Año: {self.year}")

if(__name__ == "__main__"):
    vehiculo_generico = Vehiculo("Genérica", "X1", 2005)
    vehiculo_generico.mostrar_info()

    coche1 = Coche("Toyota", "Corolla", 2020, 4)
    coche1.mostrar_info()

    moto1 = Moto("Yamaha", "R1", 2019, "Deportiva")
    moto1.mostrar_info()

    # Probando el setter
    coche1.year = 1800  # Año no válido
    coche1.year = 2022  # Año válido
    coche1.mostrar_info()
