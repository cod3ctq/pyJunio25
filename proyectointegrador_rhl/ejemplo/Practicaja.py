from ejemplo.Atm import Atm


class Practicaja(Atm):
    #Sobreescritura del metodo abstracto de la clase padre
    #ingresas el numero_cuenta y además comprar el nip
    def consultar_saldo(self):
        print("Ingrese número de cuenta")
        num_cuenta = input()
        print("Ingrese NIP")
        nip = int(input())
        #Invoca al metodo buscar cuenta
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None and cuenta.get_nip == nip:
            print("el saldo diosponiblñe es: " + str(cuenta.get_saldo()))
        else:
            print("No existe tal cuenta")
