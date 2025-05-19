class Ticket():
    def __init__(self, costo, hora):
        self.__costo = costo
        self.__hora = hora
    
    def get_costo(self):
        return self.__costo
    def set_costo(self, costo):
        self.__costo = costo
    #--------------------------------
    def get_hora(self):
        return self.__hora
    def set_hora(self,hora):
        self.__hora = hora
    #--------------------------------
    def __str__(self):
        return print(f"Precio : {self.get_costo()} a las {self.get_hora()} horas")
    #---------------------------------
    def esNoche(self):
        if "18:00" <= self.get_hora() <= "23:59":
            print(f"SI es de noche: {self.get_hora()}")
        else:
            print(f"NO es de noche: {self.get_hora()}")
    #----------------------------------
    def descuentoTotal(self, compra):
        precio_total = self.get_costo() * compra
        if 5 <= compra <= 9:
            desc = 10
            descuento = precio_total + (10/100 * precio_total)
        elif 10 <= compra:
            desc = 20
            descuento = precio_total + (20/100 * precio_total)
        else:
            desc = 0
            descuento = precio_total
        return print(f"Gracias a su compra, el descuento sera del {desc}%, El precio final a pagar es: {round(descuento, 2)}")

cliente1 = Ticket(10, "23:00")
cliente1.__str__()
cliente1.esNoche()
cliente1.descuentoTotal(10)