from Atm import Atm

class Cajero(Atm):

    def __init__(self, id,ubicacion,cuentas):
        super().__init__(id,ubicacion,cuentas)


    #Sobreescritura del metodo abstracto de la clase padre
    def consultar_saldo(self):
        print("Ingrese el numero de la cuenta")
        num_cuenta = input() #Leer desde teclado
        #Invoca al metodo buscar cuenta
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None:
            print("El saldo disponible es:" + str(cuenta.get_saldo))
        else:
            print("No existe tal cuenta")