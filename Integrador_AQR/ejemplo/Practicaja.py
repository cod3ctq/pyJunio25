from ATM import ATM

class Practicaja(ATM):
    def __init__(self, id, ubicacion, cuentas):
        super().__init__(id, ubicacion, cuentas)

    # Sobreescritura del metodo abstracto de la clase padre
    #Ingresar el numero de cuenta y además comprobar el nip
    def consultar_saldo(self):
        print("Ingrese la cuenta: ")
        num_cuenta = input()
        print("Ingrese el NIP: ")
        nip = int(input())

        # Incoca al metodo: buscar_cuenta
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None and cuenta.get_nip == nip:
            print("El saldo disponible de la cuenta es: " + str(cuenta.get_saldo))
        else:
            print("ERROR: No existe la cuenta")
