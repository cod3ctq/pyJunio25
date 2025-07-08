from Atm import Atm
from CuentaNoExisteException import CuentaNoExisteException
from LimiteExcedidoException import LimiteExcedidoException
from MontoMayorAMaximoException import MontoMayorAMaximoException
from ejemplo.BusinessException import BusinessException


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
    #Función para depositar a una cuenta

    def depositar(self, num_cuenta, monto):
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None:#Debe existir la cuenta
            if cuenta.get_max < monto:#Validar que el monto sea menor al maximo permitido
                print("Monto supera el máximo permitido de deposito en cajero")
                raise MontoMayorAMaximoException(cuenta.get_max)
            elif (cuenta.get_saldo + monto) > cuenta.get_max:#Validar que el (monto + saldo) < max
                print("La cantidad a depositar excedería el saldo máximo de la cuenta")
                raise LimiteExcedidoException(cuenta.get_max)
            else:#Depositar
                cuenta.set_saldo = cuenta.get_saldo + monto
        else:
            print("No es posible realizar el deposito. Cuenta no existe")
            raise BusinessException("No es posible realizar el deposito. Cuenta no existe: "+num_cuenta) #Lanzando la excepción

    def retirar(self, num_cuenta):
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None:
            print("Ingrese el monto a retirar: ")
            monto = float(input())

            if (monto == 0):
                raise BusinessException("El monto a retirar no puede ser 0")
            elif monto % self.get_multiplo_retirar != 0:
                raise BusinessException("El monto a retirar no es correcto solo se permiten multiplos de "+str(self.get_multiplo_retirar))
            elif cuenta.get_saldo < monto:
                raise BusinessException("Saldo insuficiente, el saldo disponible es: "+str(cuenta.get_saldo))
            else:
                cuenta.set_saldo = cuenta.get_saldo - monto
                print("El retiro se ejecutó con éxito, saldo disponible es: " + str(cuenta.get_saldo))
        else:
            raise BusinessException("La cuenta no existe")
