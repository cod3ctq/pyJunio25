class LimiteExcedidoException(Exception):
    def __init__(self, maximo):
        super().__init__(f"Al depositar se sobrepasaría del maximo saldo que puede tener la cuenta: {maximo}")