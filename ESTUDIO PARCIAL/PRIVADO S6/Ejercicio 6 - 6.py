class cliente():
    def __init__(self, dni, nom, dir, tel, corr, preferente):
        self.__dni = dni
        self.__nom = nom
        self.__dir = dir
        self.__tel = tel
        self.__corr = corr
        self.__preferente = preferente
    #--------------
    def get_dni(self):
        return self.__dni
    def set_dni(self,dni):
        if (dni.isdigit() and len(dni) == 8):
            self.__dni = dni
        else:
            print("ERROR DNI")
    #---------------
    def get_nom(self):
        return self.__nom
    def set_nom(self,nom):
        if (nom.isalpha()):
            self.__nom = nom
        else:
            print("ERROR NOMBRE")
    #---------------
    def get_dir(self):
        return self.__dir
    def set_dir(self,dir):
        if (dir.isalpha()):
            self.__dir = dir
        else:
            print("ERROR DIRECCION")
    #---------------
    def get_tel(self):
        return self.__tel
    def set_tel(self,tel):
        if (tel.isdigit() and len(tel) == 9):
            self.__tel = tel
        else:
            print("ERROR TELEFONO")
    #---------------
    def get_corr(self):
        return self.__corr
    def set_corr(self,corr):
        if (corr[0] == self.__nom[0].lower() and "@empsac.com" in corr):
            self.__corr = corr
        else:
            print("ERROR CORREO")
    #----------------
    def get_preferente(self):
        return self.__preferente
    def set_preferente(self, preferente):
        if preferente == True or preferente == False:
            self.__preferente = preferente
        elif preferente == 1:
            self.__preferente = True
        elif preferente == 2:
            self.__preferente = False
        else:
            print("ERROR PREFERENTE")
    #_---------------------------
    def ver_cliente(self):
        print(f"Dni: {self.__dni}, Nombre: {self.__nom}, Num: {self.__tel}")
        
class baseClientes ():
    def __init__(self):
        self.__lista = []
    def agregar(self, cliente):
        self.__lista.append(cliente)
        
    def actualizar_cliente(self):
        encontrado = False
        dni = input("Introducir el dni: ")
        for e in self.__lista:
            if dni == e.get_dni():
                encontrado = True
                print("QUE DESEA ACTUALIZAR")
                print("1. NOMBRE")
                print("2. DIRECCION")
                print("3. TELEFONO")
                print("4. CORREO")
                print("5. PREFERENTE")
                opcion = int(input("Ingresar la opcion: "))
                if opcion == 1:
                    nom = input("Ingresar nombre: ")
                    e.set_nom(nom)
                elif opcion == 2:
                    dir = input("Ingresar direccion: ")
                    e.set_dir(dir) 
                elif opcion == 3:
                    tel = input("Ingresar telefono: ")
                    e.set_tel(tel) 
                elif opcion == 4:
                    corr = input("Ingresar correo: ")
                    e.set_corr(corr) 
                elif opcion == 5:
                    preferente = input("Ingresar preferente: ")
                    e.set_preferente(preferente) 
                else:
                    print("Opcion INVALIDA")
                    break
        if encontrado == False:
            print("NO ENCONTRADO")
            
    def eliminar_cliente(self):
        encontrado = False
        dni = input("Introducir el dni: ")
        for e in self.__lista:
            if dni == e.get_dni():
                encontrado = True
                self.__lista.remove(e)
                
        if encontrado == False:
            print("NO ENCONTRADO")
    def buscar_cliente(self):
        encontrado = False
        dni = input("Introducir el dni: ")
        for e in self.__lista:
            if dni == e.get_dni():
                encontrado = True
                print("USUARIO ENCONTRADO")
                print(f"DNI: {e.get_dni()}")
                print(f"NOMBRE: {e.get_nom()}")
                print(f"DIRECCION: {e.get_dir()}")
                print(f"TELEFONO: {e.get_tel()}")
                print(f"CORREO: {e.get_corr()}")
                print(f"PREFERENTE: {e.get_preferente()}")
        if encontrado == False:
            print("NO ENCONTRADO")
        
    def ver_clientes(self):
        for i, e in enumerate(self.__lista, start=1):
            print(f"{i}: Dni: {e.get_dni()}, Nombre: {e.get_nom()}")

def menu ():
    print("=======BIENVENIDO=======")
    print("1. Añadir cliente")
    print("2. Buscar cliente")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Listar todos los clientes")
    print("6. Terminar")
base = baseClientes()
def main():
    try:
        while True:
            menu()
            opcion = int(input("OPCION: "))
            if opcion == 6:
                break
            elif opcion == 1:
                print("AÑADIR CLIENTE: ")
                dni = input("DNI: ")
                nom = input("NOMBRE: ")
                dir = input("DIRECCION: ")
                tel = input("TELEFONO: ")
                corr = input("CORREO: ")
                preferente_1_2 = int(input("PREFERENTE (1 OR 2): "))
                if not (dni.isdigit() and len(dni) == 8):
                    print("ERROR DNI")
                elif not (nom.isalpha()):
                    print("ERROR NOMBRE")
                elif not (dir.isalpha()):
                    print("ERROR DIRECCION")
                elif not (tel.isdigit() and len(tel) == 9):
                    print("ERROR TELEFONO")
                elif not (corr[0] == (nom[0].lower()) and "@empsac.com" in corr):
                    print("ERROR CORREO")
                elif not (preferente_1_2 == 1 or preferente_1_2 == 2):
                    print("ERROR PREFERENTE")
                else:
                    if preferente_1_2 == 1:
                        preferente = True
                    else:
                        preferente = False
                    cliente1 = cliente(dni, nom, dir, tel, corr, preferente)
                    base.agregar(cliente1)
                    print("CLIENTE GUARDADO")
                
                
            elif opcion == 2:
                base.buscar_cliente()
            elif opcion == 3:
                base.actualizar_cliente()
            elif opcion == 4:
                base.eliminar_cliente()
            elif opcion == 5:
                base.ver_clientes()
                
    except ValueError:
        print("ERROR")
main()    


