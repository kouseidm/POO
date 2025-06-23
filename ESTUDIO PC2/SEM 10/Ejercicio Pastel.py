class Pastel:
    def __init__(self, nombre, personas, precio):
        self.__nombre = nombre
        self.__personas = personas
        self.__precio = precio
        self.__ingredientes = []
        
    @property 
    def nombre (self):
        return self.__nombre
    
    @property
    def personas (self):
        return self.__personas
    
    @property
    def precio (self):
        return self.__precio
    
    def agregar_ingrediente(self, i):
        self.__ingredientes.append(i)
    
    def listar(self):
        for e in self.__ingredientes:
            print(f"Nombre: {e.nombre}")

    def contar(self):
        contador = 0
        for e in self.__ingredientes:
            contador+=1
        return contador
    
    def calorias(self):
        contador_C = 0
        for e in self.__ingredientes:
            contador_C = e.calorias + contador_C
        return contador_C
    
class Ingredientes:
    def __init__(self, nombre, medida, cantidad, calorias):
        self.__nombre = nombre
        self.__medida = medida
        self.__cantidad = cantidad
        self.__calorias = calorias
        
    @property
    def nombre (self):
        return self.__nombre
    
    @property
    def medida (self):
        return self.__medida
    
    @property
    def cantidad (self):
        return self.__cantidad
    
    @property
    def calorias (self):
        return self.__calorias
    
    
def menu():
    print ("BIENVENIDO".center(30))
    print("-"*30)
    print ("1. Ingredientes")
    print ("2. Crear pastel")
    print ("3. Agregar ingredientes")
    print ("4. Contar ingredientes del pastel")
    print ("5. Calcular las calorias del pastel")
    print ("6. Mostrar ingredientes del pastel")
    print ("0. Salir")
    print("-"*30)

lista_ingredientes = []

def main():
    try:
        while True:
            
            menu()
            opcion = int(input("Ingresar opcion: "))
            if opcion == 0:
                break
            elif opcion == 1:
                print("-"*30)
                print("REGISTRAR INGREDIENTE".center(30))
                print("-"*30)
                nombre = input("Ingresar nombre: ")
                while True:
                    unidad = input("Ingresar unidad de medida: ")
                    if unidad in ['gramos', 'puiezas', 'mililitros']:
                        break
                    else: 
                        print ("UNIDAD DE MEDIDA INCORRECTA")
                while True:
                    cantidad = int(input("Ingresar la cantidad: "))
                    if cantidad > 0:
                        break
                    else: 
                        print ("CANDIDAD -0")
                while True:
                    calorias = float(input("Ingresar las calorias por porcion: "))
                    if calorias > 0:
                        break
                    else: 
                        print ("CALORIAS -0")
                ingrediente = Ingredientes(nombre, unidad, cantidad, calorias)
                lista_ingredientes.append(ingrediente)
            elif opcion == 2:
                print("-"*30)
                print("CREAR PASTEL".center(30))
                print("-"*30)
                nombre = input("Ingresar nombre: ")
                while True:
                    cantidad = int(input("Introducir cantidad de personas: "))
                    if cantidad > 0:
                        break
                    else:
                        print("CANTIDAD DE PERSONAS EQUIVOCADO")
                while True:
                    precio = float(input("Introducir precio del Pastel: "))
                    if precio > 0:
                        break
                    else:
                        precio("PRECIO INCORRECTO")
                pastel = Pastel(nombre, cantidad, precio) 
            elif opcion == 3:
                print("-"*30)
                print("AÑADIR INGREDIENTES A PASTEL".center(30))
                print("-"*30)
                if len(lista_ingredientes) == 0:
                    print("no hay ingredientes registrados")
                else:
                    nombre_i = input("Ingresar nombre del ingrediente a agregar: ")
                    for e in lista_ingredientes:
                        if e.nombre == nombre_i:
                            pastel.agregar_ingrediente(e)
            elif opcion == 4:
                print("-"*30)
                print("CONTAR INGREDIENTES".center(30))
                print("-"*30)
                print(f"El pastel {pastel.nombre} tiene {pastel.contar()} ingredientes")
            
            elif opcion == 5:
                print("-"*30)
                print("CALORIAS".center(30))
                print("-"*30)
                print(f"El pastel {pastel.nombre} tiene {pastel.calorias()} Calorias")
            
            
            
            elif opcion == 6:
                pastel.listar()
                        

        
    except ValueError:
        print ("ERROR")

main()