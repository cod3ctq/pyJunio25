class MontoMayorAMaximoException(Exception):
    def __init__(self, maximo):
        super().__init__(f"El monto supera el máximo permitido de la cuenta:{maximo}")
