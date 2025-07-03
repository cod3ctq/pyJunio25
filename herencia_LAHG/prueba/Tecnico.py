from prueba.Empleado import Empleado

class Tecnico(Empleado):
    def __init__(self, nombre,nss,dias_vacaciones, salario_base,bono_prod):
        super().__init__(nombre, nss,dias_vacaciones, salario_base)
        self.bono_prod = bono_prod
    #El cálculo del salario del técnico es:
    #salario base + bono_productividad
    def calcular_salario(self, bono_prod):
        return self.salario_base + bono_prod

#Sobreescritura : Redefinir el como hacemos algo que hasido heredado

    def checar_entrada(self):
        print("Anota tu nombre en la libreta")
        print(self.nombre,"ha llegado")


