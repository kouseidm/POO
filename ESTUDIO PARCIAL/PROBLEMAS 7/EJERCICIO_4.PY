class representante():
    def __init__(self, dni, edad, hijosm18, ingreso, m2):
        self.__dni = dni
        self.__edad = edad
        self.__hijosm18 = hijosm18
        self.__ingreso = ingreso
        self.__m2 = m2
    #-----------------
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni
    #-----------------
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    #-----------------
    def get_hijosm18(self):
        return self.__hijosm18
    def set_hijosm18(self, hijosm18):
        self.__hijosm18 = hijosm18 
    #-----------------
    def get_ingreso(self):
        return self.__ingreso
    def set_ingreso(self, ingreso):
        self.__ingreso = ingreso 
    #-----------------
    def get_m2(self):
        return self.__m2
    def set_m2(self, m2):
        self.__m2 = m2
    #-----------------
    
    def __str__(self):
        return print(f"Dni: {self.__dni}, Edad: {self.__edad}, Hijos: {self.__hijosm18}, Ingreso: {self.__ingreso}, M2: {self.__m2}")
        
    def calificacion(self):
        calificacion = self.get_edad() + self.get_hijosm18() + (self.get_ingreso())/(self.get_m2()+1)
        return round(calificacion, 2)
    
    def monto_max(self):
        if 0 < self.calificacion() < 150:
            monto_max = 35000
        elif 150 <= self.calificacion() <= 350:
            monto_max = 45000
        else:
            monto_max = 60000
        # print(f"Cliente: {self.get_dni()}, Calificacion {self.calificacion()} , Monto max: {monto_max}") 
        return monto_max    
        
    
class base ():
    def __init__(self):
        self.__lista_repre = []
    def agregar(self, representante):
        self.__lista_repre.append(representante)
    def listado(self):
        for e in self.__lista_repre:
            print(e.get_dni(), e.get_hijosm18(), e.calificacion())
    def listado_segun_credito(self, montocredito):
        for e in self.__lista_repre:
           if e.monto_max() >= montocredito:
               print(e.get_dni(), e.monto_max()) 
    def monto_total_creditos(self):
        total = 0
        for e in self.__lista_repre:
            if e.get_hijosm18() > 2:
                total = total + e.monto_max()
        return print(total)
    def buscar_x_dni(self, dnibuscado):
        encontrado = False
        for e in self.__lista_repre:
            if e.get_dni() == dnibuscado:
                print(e.get_dni(), e.get_hijosm18(), e.calificacion(), e.monto_max())
                encontrado = True
            else:
                encontrado = False
        if encontrado == False:
            print("No encontrado...")
    

def menu():
    print("1. Ingresar representante: ")
    print("2. Lista de representante: ")
    print("3. Representantes que alcanzan credito: ")
    print("4. Mostrar monto total: ")
    print("5. Buscar por dni")
    print("6. Salir")
    
base1 = base()
def main():
    while True:
        menu()
        opcion = int(input("Ingresar opcion: "))
        if opcion == 6:
            break
        if opcion == 1:
            print("AGREGAR REPRESENTANTE")
            dni = int(input("Ingrese DNI: "))
            edad = int(input("Ingrese EDAD: "))
            hijos = int(input("Ingrese HIJOS: "))
            ingreso = int(input("Ingrese INGRESO: "))
            m2 = int(input("Ingrese M2: "))
            objeto = representante(dni,edad,hijos,ingreso,m2)
            base1.agregar(objeto)
        if opcion == 2:
            print("LISTA DE REPRESENTANTES")
            base1.listado()
        if opcion == 3:
            print("REPRESENTANTES QUE ALCANZAN MAYOR MONTO")
            monto = float(input("Ingresar el monto"))
            base1.listado_segun_credito(monto)
        if opcion == 4:
            print("MONTO TOTAL")
            base1.monto_total_creditos()
        if opcion == 5:
            print("BUSQUEDA POR DNI")
            dni= int(input("Ingresar el dni"))
            base1.buscar_x_dni(dni)
            
main()        
