from Cuenta import Cuenta
from ATM import ATM
#simula la db con la informacion de la cuentas
cuentas = [
    Cuenta("0001",15000,1000,50000,9472),
    Cuenta("0002",20000,5000,100000,2342),
    Cuenta("0003",2000,50,10000,4554),
    Cuenta("0004",30000,8000,200000,4575),
]


atm1 = ATM(10,"Boulevard San Pablo",cuentas)

try:
    atm1.depositar("0001",60000)
except Exception as error:
    print(error)

try:
    atm1.retirar("0002",16000)
except Exception as error:
    print(error)
