from Atm import Atm
class Practicaja(Atm):
    def __init__(self, id, ubicacion, cuentas):
        super().__init__(id, ubicacion, cuentas)

    #Sobreescritura del metodo abstracto de la clase padre
    # Ingresas el numero cuenta y además comparar el nip
    def consultar_saldo(self):
        print("Ingrese el numero de la cuenta")
        num_cuenta = input() #Leer desde teclado
        print("Ingrese el nip")
        nip = int(input())
        #Invoca al metodo buscar cuenta
        cuenta = self.buscar_cuenta(num_cuenta)

        if cuenta is not None and cuenta.get_nip == nip:
            print("El saldo disponible es: "+str(cuenta.get_saldo))
        else:
            print("No existe la cuenta")