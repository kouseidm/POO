class triangulo_equilatero:
    def __init__(self, lado, caracter):
        self.__lado = lado
        self.__caracter = caracter
    @property
    def lado (self):
        return self.__lado
    @property 
    def caracter (self):
        return self.__caracter
    
    def dibujar(self):
        for i in range(1, self.__lado + 1):
            espacios = ' ' * (self.__lado - i)
            if i == 1:
                linea = self.__caracter
            elif i == self.__lado:
                linea = self.__caracter * (2 * i - 1)
            else:
                linea = self.__caracter + ' ' * (2 * i - 3) + self.__caracter
            print(espacios + linea)
    
class triangulo_rectangulo:
    def __init__(self, lado1, lado2, caracter):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__caracter = caracter
    @property
    def lado1 (self):
        return self.__lado1
    @property
    def lado2 (self):
        return self.__lado2
    @property 
    def caracter (self):
        return self.__caracter
    
    def dibujar(self):
        for i in range(1, self.__lado1 + 1):
            ancho = int(self.__lado2 * i / self.__lado1)
            if ancho < 1:
                ancho = 1
            if i == 1:
                print(self.__caracter)
            elif i == self.__lado1:
                print(self.__caracter * ancho)
            else:
                if ancho > 2:
                    print(self.__caracter + ' ' * (ancho - 2) + self.__caracter)
                else:
                    print(self.__caracter * ancho)
                    

def menu():
    print("<<MENU>>".center(30))
    print("1. Triangulo equilatero")
    print("2. Triangulo rectangulo")
def main():
    while True:
        menu()
        opcion = int(input("INGRESAR OPCION: "))
        if opcion == 1:
            lado = int(input("INGRESAR LADO: "))
            if lado >= 5 and lado < 100:
                caracter = input("INGRESAR CARACTER: ")
        
                equilatero = triangulo_equilatero(lado, caracter)
                equilatero.dibujar()
        elif opcion == 2:
            lado1 = int(input("INGRESAR LADO 1: "))
            if lado1 >= 5 and lado1 < 100:
                lado2 = int(input("INGRESAR LADO 2: "))
                if lado2 > 5 and lado2 < 100:
                    caracter = input("INGRESAR CARACTER: ")
                    equilatero = triangulo_rectangulo(lado1, lado2, caracter)
                    equilatero.dibujar()

main()