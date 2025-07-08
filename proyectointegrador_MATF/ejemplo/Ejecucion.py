from Cuenta import Cuenta
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

cajero1 = Cajero(10,"Boulevard San Pablo",cuentas)#objeto hijo 1
practicaja1 = Practicaja(20,"Avenida Reforma", cuentas) #objeto hijo 2
cuenta_temp = cajero1.buscar_cuenta("0002")
cuenta_2 = practicaja1.buscar_cuenta("0004")
#print(cuenta_temp) #OK
#print(cuenta_2) #OK

#prueba del metodo consultar_saldo
#cajero1.consultar_saldo()

#practicaja1.consultar_saldo()

try:
    #cajero1.depositar("0009", 90000)
    print("Ingresa el número de cuenta")
    num_cuenta = input()
    cajero1.retirar(num_cuenta)
except Exception as e:
    print(e)