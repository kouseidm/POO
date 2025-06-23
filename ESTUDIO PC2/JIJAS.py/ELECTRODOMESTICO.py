from abc import ABC, abstractmethod

class Electrodomestico(ABC):
    def __init__(self, potencia, marca):
        self.__potecia = potencia
        self.__marca = marca
    
    @property
    def potencia (self):
        return self.__potecia
    
    @property
    def marca (self):
        return self.__marca

    @abstractmethod
    def consumo_energetico(self):
        pass
    
class Coccion(Electrodomestico):
    def __init__(self, potencia, marca, programable):
        super().__init__(potencia, marca)
        self.__programable = programable
    
    @property
    def programable (self):
        return self.__programable

class Cocina(Coccion):
    def __init__(self, potencia, marca, programable, honillas):
        super().__init__(potencia, marca, programable)
        self.__honillas = honillas
        
    def consumo_energetico(self):
        return 530
    
    @property
    def honillas (self):
        return self.__honillas
    
class Horno(Coccion):
    def __init__(self, potencia, marca, programable, capacidad):
        super().__init__(potencia, marca, programable)
        self.__capacidad = capacidad
    
    def consumo_energetico(self):
        return 280
    
    @property
    def capacidad (self):
        return self.__capacidad

horno = Horno(10,"Imaco", True, 30)
cocina = Cocina(20,"nose", False, 50)
productos = [horno, cocina]

for e in productos:
    print(e.consumo_energetico())
        