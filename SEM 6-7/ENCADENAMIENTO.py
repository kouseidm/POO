# _x_ = protejido
# __x__ = privado


# PARA ACCEDER A LOS ATRIBUTOS PRIVADOS DE UNA CLASE
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
Persona1 = Persona("Juan Perez", 50)
print(Persona1._Persona__nombre)

Persona1._Persona__edad = 55
print(Persona1._Persona__edad)