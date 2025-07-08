class Cuenta:
    def __init__(self, numero_cuenta, saldo, min, max, nip):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.min = min
        self.max = max
        self.nip = nip

    def __str__(self):
        return f"Cuenta: {self.numero_cuenta}, {self.saldo}, {self.min}, {self.max}, {self.nip}"

    @property
    def get_numero_cuenta(self):
        return self.numero_cuenta
    @property
    def get_saldo(self):
        return self.saldo
    @property
    def get_min(self):
        return self.min
    @property
    def get_max(self):
        return self.max
    @property
    def get_nip(self):
        return self.nip

    @get_numero_cuenta.setter
    def set_numero_cuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta
    @get_saldo.setter
    def set_saldo(self, saldo):
        self.saldo = saldo
    @get_min.setter
    def set_min(self, min):
        self.min = min
    @get_max.setter
    def set_max(self, max):
        self.max = max
    @get_nip.setter
    def set_nip(self, nip):
        self.nip = nip
