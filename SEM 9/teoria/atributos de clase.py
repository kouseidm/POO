class persona:
    contador = 0
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        #CONTADOR DENTRO DEL INIT (OSEA DESPUES DE CREAR UN OBJETO)
        persona.contador += 1

persona1 = persona("alexis", 20)
print(persona.contador)
persona2 = persona("Ashly", 18)
print(persona.contador)