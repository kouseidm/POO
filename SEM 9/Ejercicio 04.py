class Representante():
    def __init__ (self, dni, edad, hijos, ingreso, m2):
        self.__dni = dni
        self.__edad = edad
        self.__hijos = hijos
        self.__ingreso = ingreso
        self.__m2 = m2
    @property
    def dni (self):
        return self.__dni
    @dni.setter
    def dni (self, dni):
        self.__dni = dni
    @property
    def edad (self):
        return self.__edad
    @edad.setter
    def edad (self, edad):
        self.__edad = edad
    @property
    def hijos (self):
        return self.__hijos
    @hijos.setter
    def hijos (self, hijos):
        self.__hijos = hijos
    @property
    def ingreso (self):
        return self.__ingreso
    @ingreso.setter
    def ingreso (self, ingreso):
        self.__ingreso = ingreso
    @property
    def m2 (self):
        return self.__m2
    @m2.setter
    def m2 (self, m2):
        self.__m2 = m2
        
    
    def monto_maximo (self):
        calificacion = self.__edad + self.__hijos + (self.__ingreso)/(self.__m2 + 1)
        if 0 < calificacion < 150:
            monto_maximo = 35000
        elif 150 < calificacion < 350:
            monto_maximo = 45000
        else:
            monto_maximo = 60000 
        
        return monto_maximo

    def __str__(self):
        monto_maximo = Representante.monto_maximo(self)
        print(f"DATOS CLIENTES")
        print("-----------------")
        print(f"DNI: {self.__dni}")
        print(f"INGRESO: {self.__ingreso}")
        print(f"MONTO MAXIMO: {monto_maximo}")
        

class Base():
    def __init__(self):
        self.__lista = []
    def agregar(self, representante):
        self.__lista.append(representante)
    


cliente = Representante("07530910", 20, 3, 1700, 10)
cliente.__str__()