class LimiteExcedidoException(Exception):
    def __init__(self, maximo):
        super().__init__(f"Al depositar se sobrepasaria el máximo de la cuenta {maximo} ")