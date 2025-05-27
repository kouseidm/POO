class cuenta():
    def __init__(self ,numcta, saldo):
        self.__numcta = numcta
        self.__saldo = saldo
    @property
    def numcta(self):
        return self.__numcta 
    @numcta.setter
    def numcta(self,numcta):
        if numcta.isdigit():
            self.__numcta = numcta
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo += saldo

    #FUNCIONES
    def __str__(self):
        print (f"Numero de cuenta: {self.__numcta} con saldo {self.__saldo}")

"""
    def deposito(self, monto):
        if monto > 0 :
            self.__saldo = self.__saldo + monto
            
        else:
            print("EL MONTO INGRESADO DEBE SER MAYOR A 0")
    def retiro(self, retiro):
        if self.__saldo == "0":
            print("USTED NO TIENE s/0 FONDOS PARA RETIRAR")
        elif retiro > self.__saldo:
            print("SIN FONDOS SUFICIENTES")
        else:
            self.__saldo = self.__saldo - retiro
            
"""
class banco():
    def __init__ (self,nombre):
        self.__nombre = nombre
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if nombre.isalpha():
            self.__nombre = nombre
            
    def __str__(self):
        print(f"NOMBRE DEL BANCO : {self.__nombre}")
    #DEPENDENCIA
    def transferirDinero(self, ctaorigen, ctadestino, monto):
        if isinstance(ctaorigen, cuenta) and isinstance(ctadestino, cuenta):
            ctaorigen.saldo = -monto
            ctadestino.saldo = monto
            print(f"Se retiro a la cuenta {ctaorigen.numcta} un monto de s/{monto}")
            print( f"Se agrego a la cuenta {ctadestino.numcta} un monto de s/{monto}")
            print("<<FUNCION TERMINADA>>".center(80))
        else:
            print("NO HAY CUENTA")
       
    
      

banco1 = banco("BBVA") 

cuenta1 = cuenta(1, 200)
cuenta2 = cuenta(2, 100)
cuenta1.__str__()
cuenta2.__str__()

print("-"*30)


banco1.__str__()
monto = int(input("INGRESE LA CANTIDAD DE TRANSFERENCIA: "))
if monto >= cuenta1.saldo and monto < 0:
    print("SALDO INSUFICIENTE")
else: 
    banco1.transferirDinero(cuenta1, cuenta2, monto)
cuenta1.__str__()
cuenta2.__str__()