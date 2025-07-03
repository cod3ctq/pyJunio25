from prueba.Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, nss, dias_vacaciones, salario_base, acciones):
        super().__init__(nombre, nss, dias_vacaciones, salario_base)
        self.acciones = acciones

    #El calculo del salario del gerente es:
    #Si alcazó la meta,
    #salario_base + (1/4 de lo que tenga en acciones)

    def calcular_salario(self,meta_alcanzada):

        salario = 0
        if(meta_alcanzada):
            salario =self.salario_base + (self.acciones * 0.25)
        else:
            salario = self.salario_base + (self.acciones * 0.13)

        return salario

    #Sobreescritura
    def checar_entrada(self):
        print("Coloca tu dedo en el lector de huellas")
        print(self.nombre, "ha llegado")