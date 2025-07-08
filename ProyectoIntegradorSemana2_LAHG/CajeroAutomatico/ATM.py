from BussinessException import BussinessException
from LimiteExcedidoException import LimiteExcedidoException
from MontoMayorAMaximoException import MontoMayorAMaximoException
from MontoMayorASaldoException import MontoMayorASaldoException
from MontoMenorAMinimoException import MontoMenorAMinimoException

#Debo crear un objeto
class ATM:

    def __init__(self, id:int, ubicacion:str, cuentas):
        self.id = id
        self.ubicacion = ubicacion
        self.cuentas = cuentas

########################################################################
    def buscar_cuenta(self,num_cuenta):
        for i in self.cuentas:
            if i.num_cuenta == num_cuenta:
                return i

########################################################################
    def consultar_saldo(self):
        num_cuenta = input("Introduce un cuenta: ")
        cuenta = self.buscar_cuenta(num_cuenta)
        if cuenta is not None:
            print("El saldo disponible es:" + str(cuenta.get_saldo))
        else:
            print("No existe tal cuenta")

########################################################################
    def depositar(self, num_cuenta, monto):

        cuenta = self.buscar_cuenta(num_cuenta)
        
        if cuenta is not None:  
            if cuenta.get_max < monto:
                raise MontoMayorAMaximoException(cuenta.get_max)
            elif (cuenta.saldo + monto) > cuenta.get_max:
                raise LimiteExcedidoException(cuenta.get_max)
            else:
                cuenta.set_saldo = cuenta.get_saldo + monto
                print("Saldo despues del depósito : " + str(cuenta.get_saldo))
        else:
            raise BussinessException(f"No es posible realizar el deposito, la Cuenta {num_cuenta} no existe. " )

##########################################################################
    def retirar(self, num_cuenta, monto):
        cuenta = self.buscar_cuenta(num_cuenta)

        if cuenta is not None:
            if cuenta.get_saldo < monto:
                raise MontoMayorASaldoException(cuenta.get_min)
            elif (cuenta.saldo - monto) < cuenta.get_min:
                raise MontoMenorAMinimoException(cuenta.get_min)
            else:
                cuenta.set_saldo = cuenta.get_saldo - monto
                print("Saldo despues de actualizar : " + str(cuenta.get_saldo))
        
        else:
            raise BussinessException(f"No es posible realizar el deposito, la Cuenta {num_cuenta} no existe. ")
                