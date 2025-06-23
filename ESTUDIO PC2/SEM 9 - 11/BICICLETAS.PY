class Bicicleta:
    def __init__ (self, material, ruedas, platos):
        self.__material = material
        self.__ruedas = ruedas
        self.__platos = platos
        
    @property
    def material(self):
        return self.__material
    
    @property
    def ruedas(self):
        return self.__ruedas
    
    @property
    def platos(self):
        return self.__platos
    
class Montañera(Bicicleta):
    def __init__(self, material, ruedas, platos, suspension):
        super().__init__(material, ruedas, platos)
        self.__suspension = suspension
        self.__precioB = 1450
        
    @property
    def suspension (self):
        return self.__suspension
    @property
    def precioB (self):
        return self.__precioB
    
    def precio_final(self):
        p_sus = 0
        if self.__suspension == "RIGIDAS":
            p_sus = 250
        elif self.__suspension == "DELANTERAS":
            p_sus = 295
        elif self.__suspension == "DOBLE":
            p_sus = 600
        
        preciofinal = self.__precioB + p_sus
        return preciofinal
    def __str__(self):
        print(f"-"*20)
        print(f"TIPO DE BICICLETA: MONTAÑERA")
        print(f"-"*20)
        print(F"MATERIAL: {self.material}")
        print(f"TAMAÑO DE RUEDAS: {self.ruedas}")
        print(f"CANTIDAD DE PLATOS: {self.platos}")
        print(f"PRESENTA SUSPENSION: {self.suspension}")
        print(f"PRECIO FINAL: {self.precio_final()}")
        print(f"-"*20)
    
class Ruta(Bicicleta):
    def __init__(self, material, ruedas, platos, manubrio):
        super().__init__(material, ruedas, platos)
        self.__manubrio = manubrio
        self.__precioB = 2500
        
    @property
    def manubrio (self):
        return self.__manubrio
    @property
    def precioB (self):
        return self.__precioB
    
    def precio_final(self):
        p_man = 0
        if self.__manubrio == "DROP-BAR":
            p_man = (5*self.__precioB)/100
        elif self.__manubrio == "REGULAR-BAR":
            p_man = (7.5*self.__precioB)/100
        
        preciofinal = self.__precioB + p_man
        return preciofinal
    def __str__(self):
        print(f"-"*20)
        print(f"TIPO DE BICICLETA: RUTA")
        print(f"-"*20)
        print(F"MATERIAL: {self.material}")
        print(f"TAMAÑO DE RUEDAS: {self.ruedas}")
        print(f"CANTIDAD DE PLATOS: {self.platos}")
        print(f"MANUBRIO: {self.manubrio}")
        print(f"PRECIO FINAL: {self.precio_final()}")
        print(f"-"*20)
    
class Urbana(Bicicleta):
    def __init__(self, material, ruedas, platos, canastilla):
        super().__init__(material, ruedas, platos)
        self.__canastilla = canastilla
        self.__precioB = 900
        
    @property
    def canastilla (self):
        return self.__canastilla
    @property
    def precioB (self):
        return self.__precioB
    
    def precio_final(self):
        p_man = 0
        if self.__canastilla == "SI":
            p_man = 115
        elif self.__canastilla == "NO":
            p_man = 0
        
        preciofinal = self.__precioB + p_man
        return preciofinal
    def __str__(self):
        print(f"-"*20)
        print(f"TIPO DE BICICLETA: URBANA")
        print(f"-"*20)
        print(F"MATERIAL: {self.material}")
        print(f"TAMAÑO DE RUEDAS: {self.ruedas}")
        print(f"CANTIDAD DE PLATOS: {self.platos}")
        print(f"PRESENTA CANASTILLA: {self.canastilla}")
        print(f"PRECIO FINAL: {self.precio_final()}")
        print(f"-"*20)
    
class Tienda:
    def __init__(self):
        self.__lista = []
        
    def agregar(self, bici):
        self.__lista.append(bici)
    
    def listar(self):
        for e in self.__lista:
            print(f"-"*20)
            if isinstance(e, Ruta):
                print(f"TIPO DE BICICLETA: RUTA")
                print(f"MATERIAL: {e.material}")
                print(f"TAMAÑO DE RUEDAS: {e.ruedas}")
                print(f"CANTIDAD DE PLATOS: {e.platos}")
                print(f"MANUBRIO: {e.manubrio}")
                print(f"PRECIO FINAL: {e.precio_final()}")
            elif isinstance(e, Montañera):
                print(f"TIPO DE BICICLETA: MONTAÑERA")
                print(f"MATERIAL: {e.material}")
                print(f"TAMAÑO DE RUEDAS: {e.ruedas}")
                print(f"CANTIDAD DE PLATOS: {e.platos}")
                print(f"SUSPENSION: {e.suspension}")
                print(f"PRECIO FINAL: {e.precio_final()}")
            elif isinstance(e, Urbana):
                print(f"TIPO DE BICICLETA: URBANA")
                print(f"MATERIAL: {e.material}")
                print(f"TAMAÑO DE RUEDAS: {e.ruedas}")
                print(f"CANTIDAD DE PLATOS: {e.platos}")
                print(f"PRESENTA CANASTILLA: {e.canastilla}")
                print(f"PRECIO FINAL: {e.precio_final()}")
            print(f"-"*20)

    def cantidad_tipo(self):
        contM = 0
        contR = 0
        contU = 0
        for e in self.__lista:
            if isinstance(e, Montañera):
                contM +=1
            elif isinstance(e, Ruta):
                contR +=1
            elif isinstance(e, Urbana):
                contU +=1
        print("-"*30)  
        print(F"CONTADOR DE MONTAÑERAS {contM}")
        print(F"CONTADOR DE RUTA {contR}")
        print(F"CONTADOR DE URBANA {contU}")
        print("-"*30)
    
    def mayor_menor (self):
        mayor = self.__lista[0]
        menor = self.__lista[0]
        for e in self.__lista:
            if e.precio_final() > mayor.precio_final():
                mayor = e
            if e.precio_final() < menor.precio_final():
                menor = e
                
        print("MAYOR")
        print("-"*30)
        mayor.__str__()
        print("MENOR")
        print("-"*30)
        menor.__str__()

def menu():
    print("BIENVENIDOS".center(30))
    print("-"*30)
    print("1. Registrar Bicicleta")
    print("2. Listar bicibletas")
    print("3. Contador de bicicletas")
    print("4. Mayor y menor")
    print("0. Salir")
    print("-"*30)

#OBJETOS CREADOS
tienda = Tienda()  
bicicleta1 = Montañera('ALUMINIO', 20 , 3, 'RIGIDAS')
bicicleta2 = Montañera('CARBONO', 30, 4, 'DELANTERAS')
bicicleta3 = Ruta('TITANIO', 20, 6, 'DROP-BAR')
bicicleta4 = Ruta('TITANIO', 100, 2, 'REGULAR-BAR')
bicicleta5 = Urbana('ALUMINIO', 10, 6, 'SI')
bicicleta6 = Urbana('CARBONO',80, 2, 'NO')
tienda.agregar(bicicleta1)
tienda.agregar(bicicleta2)
tienda.agregar(bicicleta3)
tienda.agregar(bicicleta4)
tienda.agregar(bicicleta5)
tienda.agregar(bicicleta6)

def main():
    try:
        while True:
            menu()
            opcion = int(input("Ingrese opcion: "))
            if opcion == 0:
                break
            elif opcion == 1:
                print("-"*30)
                print("REGISTRAR BICICLETA")
                print("-"*30)
                print("__ELIGE EL TIPO DE BICICLETA__")
                print("(MONTAÑERA)   (RUTA)  (URBANA)")
                opcionb = input(": ").upper()
                print("-"*30)
                while True:
                    material = input("Introducir material: ").upper()
                    if material in ['ALUMINIO', 'CARBONO', 'TITANIO']:
                        break
                    else:
                        print("El material debeser:'ALUMINIO', 'CARBONO', 'TITANIO' ")
                while True:
                    ruedas = int( input("Introducir tamñao de las ruedas: "))
                    if ruedas > 0:
                        break
                    else:
                        print("El tamaño de las ruedas debe ser > 0")
                while True:
                    platos = int(input("Introducir la cantidad de platos: "))
                    if platos > 0:
                        break
                    else:
                        print("> 0")
                
                if opcionb == "MONTAÑERA":
                    while True:
                        suspension = input("Introducir suspension: ").upper()
                        if suspension in ['RIGIDAS', 'DELANTERAS', 'DOBLE']:
                            break
                        else:
                            print("'RIGIDAS', 'DELANTERAS', 'DOBLE'") 
                    montañera = Montañera(material, ruedas, platos, suspension)
                    tienda.agregar(montañera)
                elif opcionb == "RUTA":
                    while True:
                        manubrio = input("Introducir manubrio: ").upper()
                        if manubrio in ['DROP-BAR', 'REGULAR-BAR']:
                            break
                        else:
                            print('DROP-BAR', 'REGULAR-BAR') 
                    
                    ruta = Ruta(material, ruedas, platos, manubrio)
                    tienda.agregar(ruta)
                elif opcionb == "URBANA":
                    while True:
                        canastilla = input("Con canastilla?: ").upper()
                        if canastilla in ['SI', 'NO']:
                            break
                        else:
                            print("SI O NO") 
                    urbana = Urbana(material, ruedas, platos, canastilla)
                    tienda.agregar(urbana)
            
            elif opcion == 2:
                print("-"*30)
                print("LISTADO DE BICICLETAS")
                print("-"*30)
                tienda.listar()
                
            elif opcion == 3:
                tienda.cantidad_tipo()
        
            elif opcion == 4:
                tienda.mayor_menor()
                
                
            
               
    except ValueError:
        print("Error")
    
main()