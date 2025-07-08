from Cuenta import Cuenta
from ATM import ATM
from Cajero import Cajero
from Practicaja import Practicaja

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

cajero1 = Cajero(10,"Boulevard San Pablo",cuentas)#Objeto 1 hijo
practicaja1 = Practicaja(30, "Avenida Reforma", cuentas)#Objeto 2 hijo

cuenta_temp = cajero1.buscar_cuenta("0001")
cuenta_2 = practicaja1.buscar_cuenta("0003")
#print(cuenta_temp)

#prueba del metodo "consultar_saldo"
#practicaja1.consultar_saldo()

#cajero1.depositar("0001", 50000)#Llama a la función aun sin control de excepciones

"""
try:
    cajero1.depositar("0001", 100000)
except Exception as Error13:
    print(Error13)
"""

cajero1.retirar("0002", 10000)

cajero1.consultar_saldo()
