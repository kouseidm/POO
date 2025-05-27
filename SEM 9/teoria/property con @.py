class cliente ():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

cliente1 = cliente("Alexis",18)
print(cliente1.nombre)
print(cliente1.edad)
cliente1.nombre = "PEPE"
cliente1.edad = 20
print(cliente1.nombre)
print(cliente1.edad)
