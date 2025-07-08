from ATM import ATM
from ejemplo.BusinessException import BusinessException
from ejemplo.CuentaNoExisteException import CuentaNoExisteException
from ejemplo.LimiteExcedidoException import LimiteExcedidoException
from ejemplo.MontoMayorAMaximoException import MontoMayorAMaximoException


class Cajero(ATM):

    def __init__(self, id,ubicacion,cuentas):
        super().__init__(id,ubicacion,cuentas)


    #Sobreescritura del metodo abstracto de la clase padre
    def consultar_saldo(self):
        print("Ingrese el numero de la cuenta")
        num_cuenta = input() #Leer desde teclado
        #Invoca al metodo buscar cuenta
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None:
            print("El saldo disponible es: " + str(cuenta.get_saldo))
        else:
            print("No existe tal cuenta")

    def depositar(self, num_cuenta, monto):

        cuenta = self.buscar_cuenta(num_cuenta)

        if cuenta is not None:#Debe de existir la cuenta
            if cuenta.get_max < monto:#Validar que el monto sea menor al máximo permitido
                print("El monto supera el maximo permitido de depósito en cajero")
                raise MontoMayorAMaximoException(cuenta.get_max)
            elif (cuenta.get_saldo + monto) > cuenta.get_max:#Valida que el (monto+saldo) sea menor que el maximo
                print("La cantidad a depositar es excede el saldo máximo de la cuenta")
                raise LimiteExcedidoException(cuenta.get_max)
            else:
                cuenta.set_saldo = cuenta.get_saldo + monto
                print("Depósito EXITOSO")
        else:
            print("No es posible realizar el depósito. La cuenta no existe")
            raise BusinessException("No es posible realizar el depósito. La cuenta no existe: " + num_cuenta)
            #raise CuentaNoExisteException(num_cuenta)#Lanzando la excepción

    def retirar(self, num_cuenta, monto):

        cuenta = self.buscar_cuenta(num_cuenta)

        if cuenta is not None:  # Debe existir la cuenta
            if monto > cuenta.get_saldo:
                print("Fondos insuficientes para realizar el retiro")
                raise FondosInsuficientesException(cuenta.get_saldo)
            elif monto > cuenta.get_max:  # Validar que el monto no exceda el retiro máximo por transacción
                print("El monto supera el máximo permitido de retiro en cajero")
                raise MontoMayorAMaximoException(cuenta.get_max)
            else:
                cuenta.set_saldo = cuenta.get_saldo - monto
                print("Retiro EXITOSO")
        else:
            print("No es posible realizar el retiro. La cuenta no existe")
            raise BusinessException("No es posible realizar el retiro. La cuenta no existe: " + num_cuenta)

