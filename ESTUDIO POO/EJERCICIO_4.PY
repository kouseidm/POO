class ticket():
    def __init__(self, precio, hora):
        self.precio = precio
        self.hora = hora
        
    def __str__(self):
        return print(f"Ticket con el precio {self.precio} a las horas de {self.hora}")

    def esNocheHora(self):
        esNoche = False
        if "18:00" < self.hora <= "23:59" :
            esNoche = True
        return print(f"La hora de compra se realizo en la noche: {esNoche}")
    def descuentoTotal(self, n):
        precioSD = n * self.precio
        desc = 0
        if n >= 5 and n < 10:
            descuento = precioSD - (10/100 * precioSD)
            desc = 10
        elif n >= 10:
            descuento = precioSD - (20/100 * precioSD)
            desc = 20
        else:
            descuento = precioSD
            desc = 0
        return print(f"Por la compra de {n} boletos, tendra un descuento del {desc} %, pagando en total = S/{round(descuento, 2)}")

while True:
    print("<<< Bienvenidos >>>".center(80))
    print(("====="*20).center(80))
    print("PRECIO ACTUAL DEL TICKET: S/20.00")
    hora = str(input("Ingresar la hora (Hh:Mm): "))
    n = int(input("Ingresar la cantidad de boletos a commprar: "))
    ticket1 = ticket(20, hora)
    ticket1.__str__()
    ticket1.esNocheHora()
    ticket1.descuentoTotal(n)