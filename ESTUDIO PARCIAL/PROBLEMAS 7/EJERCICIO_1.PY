class cuenta():
    def __init__(self, nCuenta, saldo):
        self.__nCuenta = nCuenta
        self.__saldo = saldo
    #-------------------------
    def get_ncuenta(self):
        return self.__nCuenta
    def set_ncuenta(self, nCuenta):
        self.__nCuenta = nCuenta
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, saldo):
        self.__saldo = saldo
    def set_deposito(self, monto):
        self.__saldo = self.__saldo + monto
        print(f"El deposito de {monto} fue realizado correctamente.")
        
    def set_retiro(self, monto):
        if self.__saldo >= monto:
            self.__saldo = self.__saldo - monto
            print(f"El retiro de {monto} fue realizado correctamente.")
        else:
            print("Sin monto suficiente")
    #--------------------------
    def __str__(self):
        return print(f"Cuenta: {self.get_ncuenta()} con saldo de S/{self.get_saldo()}")
class banco():
    def __init__(self, nombre):
        self.__nombre = nombre
    #-------------------------
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    #-------------------------
    def transferirDinero(self, ctaOrigen, ctaDestino, monto):
        if isinstance(ctaOrigen, cuenta) and isinstance(ctaDestino, cuenta):
            print("Ambos pertenecen a Cuenta")
        else:
            print("No pertenecen")
            
        
        
        if ctaOrigen.get_saldo() >= monto:
            ctaOrigen.set_saldo(ctaOrigen.get_saldo() - monto)
            ctaDestino.set_saldo(ctaDestino.get_saldo() + monto)
            print(f"La transferencia de la cuenta {ctaOrigen.get_ncuenta()} a la cuenta {ctaDestino.get_ncuenta()} fue exitosa.")
        else:
            print("No hay suficiente saldo en la cuenta de origen.")
    """        
    def deposito(self, ctaDestino, monto):
        ctaDestino.set_saldo(ctaDestino.get_saldo() + monto)
        print(f"El deposito de {monto} fue realizado correctamente.")
        
    def retiro(self, ctaDestino, monto):
        if ctaDestino.get_saldo() >= monto:
            ctaDestino.set_saldo(ctaDestino.get_saldo() - monto)
            print(f"El retiro de {monto} fue realizado correctamente.")
        else:
            print("No hay suficiente dinero para retirar")
    """
            
cuenta1= cuenta("10", 300)
cuenta2 = cuenta("20", 500)
banco1 = banco("Banco1")
cuenta1.__str__()
cuenta2.__str__()
banco1.transferirDinero(cuenta1, cuenta2, 100)
cuenta1.__str__()
cuenta2.__str__()
cuenta2.set_deposito(400)
cuenta2.__str__()
cuenta1.set_retiro(200)
cuenta1.__str__()
