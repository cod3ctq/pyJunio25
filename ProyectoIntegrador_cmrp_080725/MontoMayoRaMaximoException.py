class MontoMayoraMaximoException(Exception):
    
    def __init__(self,maximo):
        super().__init__(f'el monto supera el maximo permitido en la cuenta: {cuenta}')