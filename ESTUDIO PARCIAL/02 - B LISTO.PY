class Contacto():
    def __init__(self, dni,  nombre,  telefono,  email  ):
        self.__dni = dni
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
    #--------------
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        if dni.isdigit() == True and len(dni) == 8:
            self.__dni = dni
        else:
            print("Dni incorrecto")
    #---------------
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        if nombre.isalpha() == True:
            self.__nombre = nombre
        else:
            print("Nombre incorrecto")
    #-----------------
    def get_telefono(self):
        return self.__telefono
    def set_telefono(self, telefono):
        if telefono.isdigit() == True and len(telefono) == 9:
            self.__telefono = telefono
        else:
            print("Telefono incorrecto")
    #--------------------
    def get_email(self):
        return self.__email
    def set_email(self,email):
        if "@empsac.com" in email:
            self.__email = email
        else:
            print("El email no contiene @")
    #-----------------------
    def __str__(self):
        return print(f"Dni: {self.__dni}, Nombre: {self.__nombre}, Telefono: {self.__telefono}, Email: {self.__email}")

class Agenda():
    def __init__(self):
        self.__lista = []
    def agregar (self, contacto):
        self.__lista.append(contacto)
    def actualizar (self, dni):
        encontrado = False
        for e in self.__lista:
            if e.get_dni() == dni:    
                encontrado = True
                print("1. dni")
                print("2. nombre")
                print("3. telef")
                print("4. email")
                print("5. salir")
                opcion = int(input("Que desea cambiar: "))
                if opcion == 1:
                    dni = input("Ingresar dni: ")
                    e.set_dni(dni)
                elif opcion == 2:
                    nombre = input("Ingresar nombre: ")
                    e.set_nombre(nombre)
                elif opcion == 3:
                    telef = input("Ingresar telef: ")
                    e.set_telefono(telef)
                elif opcion == 4:
                    email = input("Ingresar email: ")
                    e.set_email(email)
                else:
                    break
        if encontrado == False:
            print("No se encuentra el dni")
    def eliminar (self, dni):
        encontrado = False
        for e in self.__lista:
            if e.get_dni() == dni:
                self.__lista.remove(e)
                encontrado = True
        if encontrado == False:
            print(":c")
        if encontrado == True:
            print("ENCONTRADO")
    def buscar_nombre (self, nombre):
        encontrado = False
        for e in self.__lista:
            if e.get_nombre() == nombre:
                print(f"Dni: {e.get_dni()}")
                encontrado = True
        if encontrado == False:
            print("Usuario no encontrado")
        
        
    def mostrar (self):
        for e in self.__lista:
            print(f"Dni: {e.get_dni()}, Nombre: {e.get_nombre()}, Telefono: {e.get_telefono()}, Email: {e.get_email()}")

def menu():
    print("<<BIENVENIDO>>".center(60))
    print("=========="*3)
    print("(1)  Añadir contacto ")
    print("(2)  Buscar contacto ")
    print("(3)  Actualizar contacto ")
    print("(4)  Eliminar contacto ")
    print("(5)  Listar todos los contactos ")
    print("(6)  Terminar.")
    print("=========="*3)

agenda = Agenda()
def main():
    while True:
        menu()
        opcion = int(input("Ingresar la opcion: "))
        if opcion == 6:
            break
        if opcion == 1:
            print("<<AÑADIR CONTACTO>>".center(60))
            dni = (input("Ingresar DNI: "))
            nombre = input("Ingresar Nombre: ")
            telef = (input("Ingresar telef: "))
            email = input("Input email: ")
            if not (dni.isdigit() == True and len(dni) == 8):
                print("Dni incorrecto")
            elif not (nombre.isalpha() == True):
                print("Nombre incorrecto")
            elif not (telef.isdigit() == True and len(telef) ==9):
                print("Telefono incorrecto")
            elif "@empsac.com" not in email:
                print("Email incorrecto")
            else:
                contacto1 = Contacto(dni, nombre, telef, email)
                agenda.agregar(contacto1)
                print("CONTACTO REGISTRADO")
                print("=========="*3)
        if opcion == 2:
            print("<<BUSCAR CONTACTO>>".center(60))
            nombre = input("Ingresar nombre del usuario: ")
            agenda.buscar_nombre(nombre)
        if opcion == 3:
            print("<<ACTUALIZAR CONTACTO>>".center(60))
            dni = input("Ingresar Dni del usuario a actualizar: ")
            agenda.actualizar(dni)
        if opcion == 4:
            print("<<ELIMINAR CONTACTO>>".center(60))
            dni = input("Ingresar Dni del usuario a eliminar: ")
            agenda.eliminar(dni)
        if opcion == 5:
            print("<<MOSTRAR CONTACTOS>>".center(60))
            agenda.mostrar()
            

main()
          
          
          
# agenda = Agenda()
# contacto1 = Contacto(60914417, "alexis", 974193302, "alex@gmail.com")
# contacto2 = Contacto(12312312, "alasa", 974193302, "pepe@gmail.com")
# agenda.agregar(contacto1)
# agenda.agregar(contacto2)
# agenda.mostrar()
# agenda.actualizar(60914417)
# 
# agenda.mostrar()
# print("-"*30)

