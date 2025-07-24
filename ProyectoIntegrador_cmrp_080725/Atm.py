from abc import ABC, abstractmethod

#Una clase abstracta es aquella que contiene al menos 1 metodo abstracto
#Contiene miembros abstractos y no abstractos
class Atm(ABC): #ABC : Abstract Base Class

    def init(self, id:int, ubicacion:str, cuentas):
        self.id = id
        self.ubicacion = ubicacion
        self.cuentas = cuentas #lista de cuentas

    #metodo abstracto : metodo sin cuerpo o logica
    #pass : palabra reservada para que el compilador no marque error al no encontrar
    #un cuerpo de funcion
    @abstractmethod
    def consultar_saldo(self):
        pass

    #Recibe un numero de cuenta y busca dentro de la lista si existe tal cuenta
    #si no, imprime un mensaje
    def buscar_cuenta(self,num_cuenta):
        for temp in self.cuentas:
            if temp.numero_cuenta == num_cuenta:
                return temp


