
class Cuartel:
    def __init__(self, codigo="", nombre=""):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__unidades = []
    
    def agregar_unidades(self, unidad):
        self.__unidades.append(unidad)
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre (self):
        return self.__nombre
    
    def ataque(self):
        for e in self.__unidades:
            print(f"Unidad {e.id} atacando: {e.ataque()}")
    
    def listar(self):
        if len(self.__unidades) != 0:
            for e in self.__unidades:
                if isinstance(e,Tanque):
                    print("UNIDAD DE TANQUE")
                    print(f"Id: {e.id}")
                    print(f"Modelo: {e.modelo}")
                    print(f"Modelo de torreta: {e.torreta.modelo}")
                    print(f"Tipo de torreta: {e.torreta.tipo}")
                elif isinstance(e,Soldado):
                    print("UNIDAD DE SOLDADO")
                    print(f"Id: {e.id}")
                    print(f"Nombre: {e.nombre}")
                    print(f"Grado: {e.grado}")
        else:
            print("UNIDADES NO REGISTRADAS")
    def contar_grado(self):
        contador = 0
        contador_s = 0
        for e in self.__unidades:
            if isinstance(e, Soldado):
                contador_s += 1
                contador = e.grado + contador
        
        if contador_s == 0:
            print("NO HAY SOLDADOS")
        else:    
            print(f"El grado del cuartel es: {contador}")
    
    
class Unidad: 
    def __init__(self, id):
        self.__id = id
    
    @property
    def id (self):
        return self.__id
    
    
    
    

class Tanque(Unidad):
    def __init__(self,id, modelo, torreta):
        super().__init__(id)
        self.__modelo = modelo
        self.__torreta = torreta

    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def torreta(self):
        return self.__torreta

    def ataque(self):
        return "pow"
    
class Soldado(Unidad):
    def __init__(self,id , nombre, grado):
        super().__init__(id)
        self.__nombre = nombre
        self.__grado = grado
    
    @property
    def nombre (self):
        return self.__nombre
    
    @property
    def grado (self):
        return self.__grado

    def ataque(self):
        return "piu"
    
class Torreta:
    def __init__(self, modelo, tipo):
        self.__modelo = modelo
        self.__tipo = tipo
    
    @property
    def modelo (self):
        return self.__modelo
    
    @property
    def tipo (self):
        return self.__tipo
    
lista_soldados = []
lista_tanques = []
lista_torreta = []

def menu():
    print("BIENVENIDO".center(30))
    print("-"*30)
    print("1. Cuartel")
    print("2. Torreta")
    print("3. Tanque")
    print("4. Soldado")
    print("5. Añadir unidad")
    print("6. GRADO")
    print("7. ATACAR")
    print("8. LISTADO")
    print("0. Salir")
    print("-"*30)

    
def main():
    try:
        cuartel = Cuartel()
        while True:
            menu()
            opcion = int(input("Ingresar opcion: "))
            if opcion == 0:
                break
            elif opcion == 1:
                print("-"*30)
                print("REGISTRAR CUARTEL")
                print("-"*30)
                codigo = input("Ingresar codigo: ")
                nombre = input("Ingresar nombre: ")
                cuartel = Cuartel(codigo, nombre)
            elif opcion == 2:
                print("-"*30)
                print("REGISTRAR TORRETA")
                print("-"*30)
                modelo = input("Ingresar modelo: ")
                tipo = input("Tipo de municion: ")
                torreta = Torreta(modelo, tipo)
                lista_torreta.append(torreta)
            
            elif opcion == 3:
                print("-"*30)
                print("REGISTRAR TANQUE")
                print("-"*30)
                id = input("Ingresar Id: ")
                modelo = input("Ingresar modelo: ")
                torreta = input("Ingresar modelo torreta: ")
                torreta_obj = 0
                for e in lista_torreta:
                    if e.modelo == torreta:
                        torreta_obj = e
                        break
                if torreta_obj == 0:
                    print("Torreta no registrada")
                else:
                    tanque = Tanque(id,modelo,torreta_obj)
                    lista_tanques.append(tanque)
            
            elif opcion == 4:
                print("-"*30)
                print("REGISTRAR SOLDADO")
                print("-"*30)
                id = input("Ingresar Id: ")
                nombre = input("Ingresar nombre: ")
                while True:
                    grado = int(input("Ingresar grado: "))
                    if grado > 0 and grado < 10:
                        break
                    else:
                        print("GRADO ENTRE 0 Y 9")
                soldado = Soldado(id, nombre, grado)
                lista_soldados.append(soldado)
                        
            elif opcion == 5:
                print("-"*30)
                print("AÑADIR UNIDAD")
                print("-"*30)
                while True:
                    opcion = input(f"Que desea añadir al cuartel {cuartel.nombre}: ").upper()
                    if opcion in ['SOLDADO', 'TANQUE']:
                        break
                    else:
                        print('SOLDADO', 'TANQUE')
                if opcion == 'SOLDADO':
                    nombre = input("INGRESAR NOMBRE: ")
                    for e in lista_soldados:
                        if e.nombre == nombre:
                            cuartel.agregar_unidades(e)
                    print("UNIDAD AGREGADA")
                elif opcion == 'TANQUE':
                    while True:
                        modelo = input("INGRESAR MODELO: ")
                        for e in lista_tanques:
                            if e.modelo == modelo:
                                cuartel.agregar_unidades(e)
                        break
                            
                    print("UNIDAD AGREGADA")
            
            elif opcion == 6:
                print("-"*30)
                print("GRADO")
                print("-"*30)
                cuartel.contar_grado()
            
            elif opcion == 7:
                print("-"*30)
                print("ATACAR")
                print("-"*30)
                cuartel.ataque()
                
            elif opcion == 8:
                print("-"*30)
                print("LISTADO")
                print("-"*30)
                cuartel.listar()

    except ValueError:
        print("ERROR")
main()
    