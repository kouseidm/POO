class CuentaBancaria:
    def __init__(self, nombre, saldo, tasaInteres):
        self.nombre = nombre
        self.saldo = saldo
        self.tasaInteres = tasaInteres
    def aplicaInteres(self):
        self.saldo = self.saldo + ((self.saldo/100)*self.tasaInteres )
    def mostrarSaldo(self):
        return print(f"El saldo de la cuenta es: {self.saldo}")
    
cuenta1 = CuentaBancaria("Juan De Arona", 1000, 3)
cuenta1.aplicaInteres()
cuenta1.mostrarSaldo()

cuenta1.tasaInteres = 2
cuenta1.aplicaInteres()
cuenta1.mostrarSaldo()

