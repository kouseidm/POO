class Cuenta:
    def __init__(self, num_cuenta, saldo, num_dep, num_r, tasa, comision):
        self.num_cuenta = num_cuenta
        self.saldo = saldo
        self.num_dep = num_dep
        self.num_r = num_r
        self.tasa = tasa
        self.comision = comision
        
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo == saldo
    
    @property
    def tasa(self):
        return self.__tasa
    
    @tasa.setter
    def tasa(self,tasa):
        self.__tasa = tasa
        
    def depositar_dinero (self, monto):
        if monto > 0:
            self.saldo += monto
            print("Dinero depositado correctamente")
    
    def retirar_dinero (self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Usted no cuenta con el saldo suficiente")
    
    def calcular_interes (self):
        interes = self.saldo * self.tasa