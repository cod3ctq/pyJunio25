class LimiteExcedidoException(Exception):
    def __init__(self, maximo):
        super().__init__(f"Al depositar se excede el límite de cuenta:{maximo} ")