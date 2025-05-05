class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def imprimir(self):
        
        print(f"({self.x}, {self.y})")
    def imprimir_cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Primer cuadrange")
        elif self.x < 0 and self.y > 0:
            print("Segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        else:
            print("Cuarto cuadrante")
    # Programa principal
punto1 = Punto(10, -2)
punto1.imprimir()
punto1.imprimir_cuadrante()