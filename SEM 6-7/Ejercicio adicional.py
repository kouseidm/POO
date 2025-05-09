"""
Desarrollar una aplicación que pueda gestionar las 
personas (registrar y reportar información sobre personas). 
Cada persona debe tener: •un nombre •una edad El sistema 
debe permitir generar dos reportes: uno con todas las 
personas y otra con personas filtrados por edad. Las 
personas están almacenados en una basePersonas 
(la basePersonas tiene como atributo una lista de personas) 
Clase Persona (con los atributos descritos y el 
método verpersona [muestra los datos de una persona])
Clase basePersonas (listapersonas (lista que almacena 
objetos Persona) y los métodos: registrarPersona 
[agrega una persona a la basePersonas], visualizarPersonas 
[ver listado de personas]
"""

class persona():
    def __init__ (self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    #metodo de acceso
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    #------------------
def registrar():
    nombre1 = input("Introducir el nombre: ")
    edad1 = input("Ingresar la edad: ")
    persona1 = persona(nombre1, edad1)
    print(persona1)
registrar()