class CuentaNoExisteException(Exception):
    def __init__(self, numero_cuenta):
        super().__init__(f"No existe la cuenta con el número: {numero_cuenta}")

