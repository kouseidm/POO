import math

class circulo:
    def __init__ (self, radio):
        self.radio= radio
    def area(self):
        return math.pi * self.radio**2
    def circunferencia(self):
        return 2*math.pi * self.radio
    
circulo1 = circulo(5)
circulo2 = circulo(2)
circulo3 = circulo(6)
area1 = round(circulo1.area(),2)

print(f"El area del circulo1 es {area1}")
print(f"El area del circulo2 es {round(circulo2.area(),2)}")
print(f"El area del circulo3 es {round(circulo3.area(),2)}")
print(f"La circunferencia del circulo1 es {circulo1.circunferencia()}")
print(f"La circunferencia del circulo2 es {circulo2.circunferencia()}")
print(f"La circunferencia del circulo3 es {circulo3.circunferencia()}")

    