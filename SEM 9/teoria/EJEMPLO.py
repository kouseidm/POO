class Cliente:
    __contador = 0
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        Cliente.__contador += 1
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @classmethod
    def get_contador(cls):
        return cls.__contador

    @classmethod
    def set_contador(cls,contador):
        cls.__contador =  contador
        
   

Cliente1 = Cliente("Alexis", 20)
Cliente1.nombre = "KJSHADKSAJD"
print(Cliente1.nombre)
