from prueba.Empleado import Empleado
from prueba.Tecnico import Tecnico
from prueba.Gerente import Gerente

class Main:

    empleado_generico = Empleado("Omar", "O2MRBGTR",12,13000)

    empleado_generico.set_nombre = "Kevin"
    empleado_generico.checar_entrada()
    empleado_generico.checar_salida()



    tecnico1 = Tecnico("Julian", "JUEJDLA",15,15000,1500)
    tecnico1.set_nombre = "Daniel"
    tecnico1.checar_entrada()
    tecnico1.checar_salida()


    gerente =  Gerente("Omar", "O2MRBGTR",12,17000,15000)
    print(tecnico1.calcular_salario(2000))

    print(gerente.calcular_salario(True))