from ejemplo.Atm import Atm
from ejemplo.BussinessException import BussinessException
from ejemplo.CuentaExistrException import CuentaNoExisteException
from ejemplo.LiminteExcedidoException import LimiteExcedidoException
from ejemplo.MontoMayoRaMaximoException import MontoMayoraMaximoException

class Cajero(Atm):

    def __init__(self, id, ubicacion, cuentas):
        super().init(id, ubicacion, cuentas)

    # Sobreescritura del metodo abstracto de la clase padre
    def consultar_saldo(self):
        print("Ingrese el numero de la cuenta")
        num_cuenta = input()  # Leer desde teclado
        # Invoca al metodo buscar cuenta
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None:
            print("El saldo disponible es:" + str(cuenta.get_saldo))
        else:
            print("No existe tal cuenta")

    # Funcion para depositar a una cuenta
    def depositar(self, num_cuenta, monto):
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None:  # Debe existir la cuenta
            if cuenta.get_max < monto:  # Validar que el monto sea menor al maximo permitido
                print("Monto supera el maximo permitido de deposito en cajero")
                raise MontoMayorAMaximoException(cuenta.get_max)
            elif (cuenta.get_saldo + monto) > cuenta.get_max:  # Validar que el (monto + saldo) < max
                print("Cantidad a depositar excederia el saldo maximo de la cuenta")
                raise LimiteExcedidoException(cuenta.get_max)
            else:  # Depositar
                cuenta.set_saldo = cuenta.get_saldo + monto
        else:
            print("No es posible realizar el deposito. Cuenta no existe")
            raise BusinessException("No es posible realizar el deposito. Cuenta no existe:",
                                    num_cuenta)  # Lanzando la excepcion
            # raise CuentaNoExisteException(num_cuenta) #Lanzando la excepcion

    def retirar_cajero(self,num_cuenta,monto_retiro):
            cuenta = self.buscar_cuenta(num_cuenta)
            if cuenta is not None:
                if cuenta.saldo < monto_retiro:
                    print("Monto a retirar supera el saldo disponible")
                    raise SaldoInsuficienteException(cuenta.saldo)
                else:
                    cuenta.set_saldo = cuenta.get_saldo - monto_retiro
            else:
                print("No es posible realizar el retiro. Cuenta no existe")
                raise BusinessException("No es posible realizar el retiro. Cuenta no existe:",
                                        num_cuenta)  # Lanzando la excepcion