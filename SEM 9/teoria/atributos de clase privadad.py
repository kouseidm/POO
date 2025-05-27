class persona:
    __contador = 0
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        #CONTADOR DENTRO DEL INIT (OSEA DESPUES DE CREAR UN OBJETO)
        persona.__contador += 1

    @classmethod
    def get_contador(cls):
        return cls.__contador
    
    @classmethod
    def set_contador(cls,contador):
        cls.__contador = contador
    
persona1 = persona("alexis", 20)
print("="*30)
print(persona.get_contador())
print("="*30)
print(persona1.nombre)
print(persona1.edad)
print("="*30)
persona.set_contador(10)

persona2 = persona("Ashly", 18)
print("="*30)
print(persona2.nombre)
print(persona2.edad)
print("="*30)
print(persona.get_contador())

