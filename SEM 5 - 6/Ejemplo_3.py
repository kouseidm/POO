class Cuenta:
    def __init__(self, numCta, saldo):
        self.numCta = numCta
        self.saldo = saldo
    def deposito(self, monto):
        self.saldo += monto
    def retiro(self, monto):
        self.saldo -= monto
    def imprimeSaldo(self):
        print(f"Saldo de la cuenta {self.numCta} es {self.saldo}")
        
class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
    def transferirDinero(self, ctaOrigen, ctaDestino, monto):
        if ctaOrigen.numCta != ctaDestino.numCta:
            if ctaOrigen.saldo >= monto:
                ctaOrigen.retiro(monto)
                ctaDestino.deposito(monto)
                print("Transferencia exitosa")
            else:
                print(f"Fondos insuficientes en cuenta {ctaOrigen.numCta} ")
        else:
            print("No se puede transferir hacia si mismo")
            
banco = Banco("El usurero")
print(f"\nBanco: {banco.nombre}")
cuenta1 = Cuenta(123, 1000)
cuenta1.imprimeSaldo()
cuenta2 = Cuenta(345, 300)
cuenta2.imprimeSaldo()
banco = Banco("El usurero")
print("="*30)
banco.transferirDinero(cuenta1, cuenta2, 300)
print("="*30)
print(f"\nBanco: {banco.nombre}")
cuenta1.imprimeSaldo()
cuenta2.imprimeSaldo()
print("="*30)