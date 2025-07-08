class SaldoInsuficienteException(Exception):

    def __init__(self, saldo):
        super().__init__(f'el monto supera el maximo permitido en la cuenta: {cuenta}')