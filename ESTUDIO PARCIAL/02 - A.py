lista_integrantes = []
lista_proyectos = []
class integrante():
    def __init__ (self, cod, nombre):
        self.__cod = cod 
        self.__nombre = nombre
        lista_integrantes.append(self)
    #----------------------
    def get_cod(self):
        return self.__cod
    def set_cod(self, cod):
        if cod.isdigit() == True and len(cod) == 4:
            self.__cod = cod
        else:
            print("ERROR CODIGO")
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        if nombre.isalpha():
            self.__nombre = nombre
        else:
            print("ERROR NOMBRE") 
    def mostrarI(self):
        return print(f"Codigo: {self.__cod}, Nombre: {self.__nombre}")
    #------------------------

class proyecto():
    def __init__ (self, Pnro, Pnombre):
        self.__Pnro = Pnro
        self.__Pnombre = Pnombre
        self.__lista = []
        
    def get_Pnro(self):
        return self.__Pnro
    def set_Pnro(self, Pnro):
        if Pnro > 0:
            self.__Pnro = Pnro
        else:
            print("ERROR CODIGO")
    def get_Pnombre(self):
        return self.__Pnombre 
    def set_Pnombre(self, Pnombre):
        if Pnombre.isalpha():
            self.__Pnombre = Pnombre
        else:
            print("ERROR NOMBRE")   
    #-------------------
    def agregar(self, integrante, rol):
        for e in lista_integrantes:
            if integrante == e:
                self.__lista.append(integrante)
        print("INTEGRANTE GUARDADO")
    def eliminar(self, cod):
        Encontrado = False
        for e in self.__lista:
            if e.get_cod() == cod:
                self.__lista.remove(e)
                Encontrado = True
        if Encontrado == False:
            print("no encontrado")
        
    def mostrar(self):
        for e in self.__lista:
            print(f"Proyecto {self.__Pnro}: {self.__Pnombre}, Codigo: {e.get_cod()}, Nombre: {e.get_nombre()}")
class TOTALPROYECTOS():
    def __init__(self):
        self.__lista_P = []
    def agregar(self, proyecto):
        self.__lista_P.append(proyecto)
    def mostrar(self):
        for e in self.__lista_P:
            print(f"Proyecto {e.get_Pnro()}: {e.get_Pnombre()}")
            for i in e._proyecto__lista:
                print(f"  Codigo: {i.get_cod()}, Nombre: {i.get_nombre()}")
                
                
                
proyecto1 = proyecto(1, "Poo")
Total = TOTALPROYECTOS()
integrante1 = integrante(4020, "Alexis")
integrante2 = integrante(1000, "pepe")
integrante1.mostrarI()
integrante2.mostrarI()
proyecto1.agregar(integrante1)
proyecto1.agregar(integrante2)
proyecto1.mostrar()
Total.agregar(proyecto1)
Total.mostrar()
proyecto1.eliminar(4020)
proyecto1.mostrar()
Total.mostrar()
