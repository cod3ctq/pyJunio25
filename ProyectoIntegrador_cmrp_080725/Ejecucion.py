from ejemplo.Cuenta import Cuenta
from ejemplo.Atm import Atm
from ejemplo.Cajero import Cajero
from ejemplo.PractiCaja import Practicaja

#Definir la lista con las cuentas cargadas
#simula la db con la informacion de la cuentas
cuentas = [
    Cuenta("0001",15000,1000,50000,9472),
    Cuenta("0002",20000,5000,100000,2342),
    Cuenta("0003",2000,50,10000,4554),
    Cuenta("0004",30000,8000,200000,4575),
]

#Debido a que Atm es una clase abstracta, no es posible instanciarla
#En su lugar, se instancian las clases que heredaron de ella para
#darle un uso a ese codigo
#atm = Atm(10,"Boulevard San Pablo",cuentas)

cajero1 = Cajero(10,"Boulevard San Pablo",cuentas) #objeto hijo 1
practicaja1 = Practicaja(20,"Avenida Reforma",cuentas) #objeto hijo 2

#cuenta_temp = cajero1.buscar_cuenta("0002")
#cuenta_2 = practicaja1.buscar_cuenta("0004")
#print(cuenta_2) #OK

#prueba del metodo consultar_saldo
#cajero1.consultar_saldo()
#practicaja1.consultar_saldo()

#llamada a la funcion aun sin control de excepciones
'''
try:
    cajero1.depositar('0001',5000)

except Exception as error:
    print(error)

cajero1.consultar_saldo()
'''

## Logica de retiro de saldo
try:
    cajero1.consultar_saldo()
    cajero1.retirar_cajero('0001',1000)
    cajero1.consultar_saldo()
except Exception as error:
    print(error)




