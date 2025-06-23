class Agencia: 
    def __init__ (self, tamaño):
        self.__tamaño = tamaño
        self.__contactos = []
        
    @property
    def tamaño (self):
        return self.__tamaño

    def agregar (self, contacto):
        if isinstance(contacto, Contacto):
            self.__contactos.append(contacto)
        else: 
            print("El contacto debe ser un objeto existente")

    def existe (self, nombre):
        existe = False
        for e in self.__contactos:
            if e.nombre == nombre and isinstance(e,Contacto):
                existe = True
        return existe    
    def listar (self):
        for e in self.__contactos:
            print(f"Nombre: {e.nombre}")
            e.listar_numero()
            print("-"*30)
    def buscar (self, nombre):
        for e in self.__contactos:
            if e.nombre == nombre:
                e.__str__()
            
    
    def eliminar (self, nombre):
        for e in self.__contactos:
            if e.nombre == nombre:
                self.__contactos.remove(e)
                print("ELIMINADO")
                
    def agenda_llena (self):
        if len(self.__contactos) == self.__tamaño:
            print(f"LA AGENDA YA ESTA LLENA CON {len(self.__contactos)} contactos")
        else:
            print(f"LA AGENDA NO ESTA LLENA CON {len(self.__contactos)} contactos")
    
    def huecos (self):
        num_c = len(self.__contactos)
        num_t = self.__tamaño
        huecos = num_t - num_c
        print(f"La cantidad de huecos actuales son: {huecos}")

class Contacto:
    def __init__(self, nombre, numeros):
        self.__nombre = nombre
        self.__numeros = []
        self.agregar(numeros)
    
    @property 
    def nombre (self):
        return self.__nombre

    def agregar (self, num):
        self.__numeros.append(num)
    def listar_numero(self):
        for i, e  in enumerate(self.__numeros,start=1):
            print(i, self.__numeros[i-1])
            
    def __str__(self):
        print(f"Nombre: {self.nombre}")
        self.listar_numero()

def menu():
    print("-"*30)
    print("BIENVENIDO".center(30))
    print("-"*30)
    print("1. Crear contacto")
    print("2. Agregar numero a contacto")
    print("3. Crear Agenda")
    print("4. Añadir contacto a agenda")
    print("5. Existe contacto")
    print("6. Listar")
    print("7. Buscar contacto")
    print("8. Eliminar contacto")
    print("9. Agenda llena")
    print("10. Huecos libles")
    print("0. Salir")
    print("-"*30)

lista_contactos = []
def main():
    try:
        while True:
            menu()
            opcion = int(input("Ingresar opcion: "))
            if opcion == 0:
                break
            elif opcion == 1:
                print("-"*30)
                print("CREAR CONTACTO")
                print("-"*30)
                nombre = input("Ingresar nombre: ")
                while True:
                    numero = int(input("Ingresar numero: "))
                    if numero > 0 and len(str(numero)) == 9:
                        break
                    else:
                        print("NUMERO INCORRECTO")
                
                
                contacto = Contacto(nombre, numero)
                lista_contactos.append(contacto)
            elif opcion == 2:
                print("-"*30)
                print("AÑADIR NUMERO A CONTACTO")
                print("-"*30)
                nombre = input("Ingresar nombre: ")
                existe = 0
                for e in lista_contactos:
                    if e.nombre == nombre:
                        existe = 1
                        while True:
                            numero = int(input("Ingresar numero: "))
                            if numero > 0 and len(str(numero)) == 9:
                                break
                            else:
                                print("NUMERO INCORRECTO")
                        e.agregar(numero)
                if existe == 0:
                    print("CONTACTO NO REGISTRADO")
                    
            elif opcion == 3:
                print("-"*30)
                print("CREAR AGENDA")
                print("-"*30)
                while True:
                    opcion = input("DESEA SELECCIONAR TAMAÑO: ").upper()
                    if opcion in ['SI', 'NO']:
                        break
                    else:
                        print("OPCION INCORRECTA")
                if opcion == "SI":
                    while True:
                        tamaño = int(input("Ingresar tamaño: "))
                        if tamaño > 0:
                            break
                        else:
                            print("tamaño INCORRECTO")
                else:
                    tamaño = 10
                agenda = Agencia(tamaño)
            elif opcion == 4:
                print("-"*30)
                print("AGREGAR CONTACTO A AGENDA")
                print("-"*30)
                nombre = input("Ingresar nombre: ")
                for e in lista_contactos:
                    if e.nombre == nombre:
                        agenda.agregar(e)
            elif opcion == 5:
                print("-"*30)
                print("EXISTE CONTACTO")
                print("-"*30)
                nombre = input("Ingresar nombre: ")
                print(agenda.existe(nombre))
            elif opcion == 6:
                print("-"*30)
                print("LISTAR")
                print("-"*30)
                agenda.listar()
            elif opcion == 7:
                print("-"*30)
                print("BUSCAR")
                print("-"*30)
                nombre = input("Ingresar nombre: ")
                agenda.buscar(nombre)
            elif opcion == 8:
                print("-"*30)
                print("ELMINIAR")
                print("-"*30)  
                nombre = input("Ingresar nombre: ")
                agenda.eliminar(nombre)   
            elif opcion == 9:
                print("-"*30)
                print("AGENDA LLENA")
                print("-"*30)
                agenda.agenda_llena()
            elif opcion == 10:
                print("-"*30)
                print("HUECOS")
                print("-"*30)
                agenda.huecos()     
    except ValueError:
        print("ERROR")
    
main()
num1 = 987654321
num2 = 987653321
num3 = 987654231
contacto = Contacto("pepe")
contacto.agregar(num1)
contacto.agregar(num2)
contacto.agregar(num3)


agencia = Agencia()
agencia.agregar(contacto)
agencia.buscar("pepe")

agencia.agenda_llena()

agencia.huecos()

