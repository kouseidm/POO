class Autos:
    lista_autos = []
    def __init__(self, marca="", material="", transmision="", cilindrada=0):
        self.__marca = marca
        self.__material = material
        self.__transmision = transmision
        self.__cilindrada = cilindrada
    @property
    def marca(self):
        return self.__marca
    @property
    def material(self):
        return self.__material
    @property
    def transmision(self):
        return self.__transmision
    @property
    def cilindrada(self):
        return self.__cilindrada
    
    @classmethod
    def agregar(cls, auto):
        cls.lista_autos.append(auto)
        
    @classmethod
    def listar_todo(cls):
        for e in cls.lista_autos:
            if isinstance(e, Sedan):
                print("-"*30)
                print("___SEDAN___")
                print(f"Marca: {e.marca}")
                print(f"Material: {e.material}")
                print(f"Transmision: {e.transmision}")
                print(f"Cilindrada: {e.cilindrada}")
                print(f"Suspension: {e.suspension}")
                print(f"PRECIO FINAL: {e.precio_final()}")
                print("-"*30)
            if isinstance(e, Hatchback):
                print("-"*30)
                print("___HATCHBACK___")
                print(f"Marca: {e.marca}")
                print(f"Material: {e.material}")
                print(f"Transmision: {e.transmision}")
                print(f"Cilindrada: {e.cilindrada}")
                print(f"Tiempo: {e.tiempo}")
                print(f"PRECIO FINAL: {e.precio_final()}")
                print("-"*30)
            if isinstance(e, Convertibles):
                print("-"*30)
                print("___CONVERTIBLES___")
                print(f"Marca: {e.marca}")
                print(f"Material: {e.material}")
                print(f"Transmision: {e.transmision}")
                print(f"Cilindrada: {e.cilindrada}")
                print(f"Maletera?: {e.maletera}")
                print(f"PRECIO FINAL: {e.precio_final()}")
                print("-"*30)
                
    @classmethod
    def mayor_menor(cls):
        mayor = cls.lista_autos[0]
        menor = cls.lista_autos[0]
        for e in cls.lista_autos:
            if e.precio_final() > mayor.precio_final():
                mayor = e
            if e.precio_final() < menor.precio_final():
                menor = e
        print("-"*30) 
        print("MENOR")
        menor.__str__()
        print("-"*30) 
        print("MAYOR")
        mayor.__str__()
        
    @classmethod
    def orden_mayor_meno(cls):
        lista_ordenada = sorted(cls.lista_autos, key=lambda x: x.precio_final(), reverse=True)
        for e in lista_ordenada:
            e.__str__()
        
    @classmethod
    def orden_mayor_menor_especifico(cls, tipo):
        sedan_lista = []
        hatch_lista = []
        convertible = []
        for e in cls.lista_autos:
            if isinstance(e, Sedan):
                sedan_lista.append(e)
            elif isinstance(e, Hatchback):
                hatch_lista.append(e)
            elif isinstance(e, Convertibles):
                convertible.append(e)
        
        
        if tipo == "SEDAN":
            lista_orden = sorted(sedan_lista, key=lambda x: x.precio_final(), reverse=True)
        elif tipo == "HATCHBACK":
            lista_orden = sorted(hatch_lista, key=lambda x: x.precio_final(), reverse=True)
        elif tipo == "CONVERTIBLES":
            lista_orden = sorted(convertible, key=lambda x: x.precio_final(), reverse=True)
        
        for e in lista_orden:
            e.__str__()
    
    

class Sedan(Autos):
    def __init__(self, marca, material, transmision, cilindrada, suspension):
        super().__init__(marca, material, transmision, cilindrada)
        self.__suspension = suspension
        self.__precioB = 40000
    
    @property
    def suspension(self):
        return self.__suspension
    
    def precio_final(self):
        añadido = 0
        if self.suspension == 'POSTERIOR':
            añadido = 1400
        elif self.suspension == 'DELANTERA':
            añadido = 1500
        elif self.suspension == 'DOBLE':
            añadido = 1800
        return self.__precioB + añadido
    
    def __str__(self):
        print("-"*30)
        print("___SEDAN___")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Transmision: {self.transmision}")
        print(f"Cilindrada: {self.cilindrada}")
        print(f"Suspension: {self.suspension}")
        print(f"PRECIO FINAL: {self.precio_final()}")
        print("-"*30)
    

class Hatchback(Autos):
    def __init__(self, marca, material, transmision, cilindrada, tiempo):
        super().__init__(marca, material, transmision, cilindrada)
        self.__tiempo = tiempo
        self.__precioB = 44000
        
    @property
    def tiempo(self):
        return self.__tiempo
    
    def precio_final(self):
        añadido = 0
        if self.tiempo == 2:
            añadido = (20*self.__precioB)/100
        elif self.tiempo == 4:
            añadido = (10*self.__precioB)/100
        return self.__precioB + añadido
    
    def __str__(self):
        print("-"*30)
        print("___HATCHBACK___")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Transmision: {self.transmision}")
        print(f"Cilindrada: {self.cilindrada}")
        print(f"Tiempo: {self.tiempo}")
        print(f"PRECIO FINAL: {self.precio_final()}")
        print("-"*30)

class Convertibles(Autos):
    def __init__(self, marca, material, transmision, cilindrada, maletera):
        super().__init__(marca, material, transmision, cilindrada)
        self.__maletera = maletera
        self.__precioB = 50000
        
    @property
    def maletera(self):
        return self.__maletera
    
    def precio_final(self):
        añadido = 0
        if self.maletera == "SI":
            añadido = 5000
        elif self.maletera == "NO":
            pass
        return self.__precioB + añadido

    def __str__(self):
        print("-"*30)
        print("___CONVERTIBLES___")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Transmision: {self.transmision}")
        print(f"Cilindrada: {self.cilindrada}")
        print(f"Maletera?: {self.maletera}")
        print(f"PRECIO FINAL: {self.precio_final()}")
        print("-"*30)
    

def menu():
    print("BIENVENIDO".center(30))
    print("1. Registrar Auto: ")
    print("2. Listar Autos: ")
    print("3. Menor Mayor")
    print("4. Orden mayor a menor total")
    print("5. Orden mayor a menor total por tipo")
    print("0. Salir")

def main():
    try:
        autos = Autos()
        objeto1 = Sedan('TOYOTA', 'ALUMINIO', 'MECANICA', 30, 'POSTERIOR')
        objeto2 = Sedan('MERCEDES', 'CARBONO', 'ELECTRICO', 20, 'DOBLE')
        objeto3 = Sedan('TOYOTA', 'ALUMINIO', 'MECANICA', 15, 'DELANTERA')
        objeto4 = Hatchback('TOYOTA', 'ALUMINIO', 'MECANICA', 23, 2)
        objeto5 = Hatchback('MERCEDES', 'CARBONO', 'AUTOMATICA', 32, 4)
        objeto6 = Hatchback('TOYOTA', 'ALUMINIO', 'MECANICA', 36, 2)
        objeto7 = Convertibles('TOYOTA', 'ALUMINIO', 'AUTOMATICA', 54, 'SI')
        objeto8 = Convertibles('MERCEDES', 'CARBONO', 'ELECTRICO', 33, 'SI')
        objeto9 = Convertibles('TOYOTA', 'ALUMINIO', 'MECANICA', 12, 'NO')
        autos.agregar(objeto1)
        autos.agregar(objeto2)
        autos.agregar(objeto3)
        autos.agregar(objeto4)
        autos.agregar(objeto5)
        autos.agregar(objeto6)
        autos.agregar(objeto7)
        autos.agregar(objeto8)
        autos.agregar(objeto9)
        
        while True:
            menu()
            opcion = int (input ("Ingresar opcion: "))
            if opcion == 0:
                break
            elif opcion == 1:
                print("-"*30)
                print("REGISTRAR AUTOS")
                print("['SEDAN','HATCHBACK','CONVERTIBLES']")
                print("-"*30)
                while True:
                    opcion1 = input("Ingresar opcion: ").upper()
                    if opcion1 in ['SEDAN','HATCHBACK','CONVERTIBLES']:
                        break
                    else:
                        print("ERROR")
                marca = input("Introducir marca: ")
                material = input("Ingresar tipo de material: ").upper()
                while True:
                    transmision = input("Ingresar tipo de transmision: ").upper()
                    if transmision in ['AUTOMATICA','MECANICA','ELECTRICO']:
                        break
                    else:
                        print("ERROR transmision")
                while True:
                    cilindrada = float(input("Introducir cilindrada"))
                    if cilindrada >0:
                        break
                    else:
                        print("ERROR -0")
                if opcion1 == "SEDAN":
                    while True:
                        suspension = input("Ingresar tipo de suspension: ").upper()
                        if suspension in ['POSTERIOR','DELANTERA','DOBLE']:
                            break
                        else:
                            print("ERROR suspension")       
                    sedan = Sedan(marca, material, transmision, cilindrada, suspension)
                    autos.agregar(sedan)
                elif opcion1 == "HATCHBACK":
                    while True:
                        tiempo = int(input("Ingresar tiempo de encendido: "))
                        if tiempo == 4 or tiempo == 2:
                            break
                        else:
                            print("ERROR tiempo")       
                    hatchback = Hatchback(marca, material, transmision, cilindrada, tiempo)
                    autos.agregar(hatchback)
                elif opcion1 == "CONVERTIBLES":
                    while True:
                        maletera = input("Tiene maletera?: ").upper()
                        if maletera in ['SI', 'NO']:
                            break
                        else:
                            print("ERROR maletera")       
                    convertibles = Convertibles(marca, material, transmision, cilindrada, maletera)
                    autos.agregar(convertibles)
            elif opcion == 2:
                print("-"*30)
                print("LISTAR AUTOS")
                print("-"*30)
                autos.listar_todo()
            elif opcion == 3:
                autos.mayor_menor()
            
            elif opcion == 4:
                autos.orden_mayor_meno()
                
            elif opcion == 5:
                print("-"*30)
                print("ODENADO SEGUN TIPO")
                print("-"*30)
                while True:
                    tipo = input("INGRESAR TIPO (SEDAN','HATCHBACK','CONVERTIBLES): ").upper()
                    if tipo in ['SEDAN','HATCHBACK','CONVERTIBLES']:
                        break
                    else:
                        print("ERROR")
                autos.orden_mayor_menor_especifico(tipo)
               
                
        
    except ValueError:
        print("Error")
    
    
main()
    
    