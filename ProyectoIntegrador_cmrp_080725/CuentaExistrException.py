class CuentaNoExisteException(Exception):

    def __init__(self,num_cuenta):
        super().__init__(f'no existe la cuenta:{num_cuenta}')