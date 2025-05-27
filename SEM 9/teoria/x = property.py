class Rectangulo:
#Constructor
    def __init__(self, largo, ancho):
#Atributos de instancia
        self.__largo = largo
        self.__ancho = ancho
#Métodos de acceso
    def __get_largo(self):
        return self .__largo
    def __set_largo(self, largo):
        self.__largo = largo
        
    largo = property(__get_largo, __set_largo)
    
    def  __set_ancho(self, ancho):
        self.__ancho = ancho
        
    ancho = property(fset = __set_ancho)
#Métodos de instancia
    def area(self):
        return self.__largo * self.__ancho

Rectangulo1 = Rectangulo(10,5)
Rectangulo1.largo = 4
Rectangulo1.ancho = 10
print(Rectangulo1.area())