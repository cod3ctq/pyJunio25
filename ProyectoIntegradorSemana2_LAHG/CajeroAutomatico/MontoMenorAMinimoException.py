class MontoMenorAMinimoException(Exception):
    def __init__(self, min):
        super().__init__(f"El monto supera el minimo permitido de la cuenta:{min}")