class Almacen():
    def __init__ (self):
        self.__productos = []
        self.__proveedores = []
        
    def agregar_producto (self, producto):
        self.__productos.append(producto)
        print("-"*30)
        print("PRODUCTO AGREGADO".center(30))
        print("-"*30)
    
    def agregar_provedor (self, provedor):
        self.__proveedores.append(provedor)
        print("-"*30)
        print("PROVEEDOR AGREGADO".center(30))
        print("-"*30)    
    
    def listar_productos(self):
        print("-"*30)
        print("LISTADO DE PRODUCTOS".center(30))
        print("-"*30)
        for e in self.__productos:
            print(f"ID PRODUCTO: {e.idProducto}")
            print(f"NOMBRE: {e.nombre}")
            print(f"TIPO: {e.tipo}")
            print("-"*30)
    
    def listar_proveedores(self):
        print("-"*30)
        print("LISTADO DE PROVEEDORES".center(30))
        print("-"*30)
        for e in self.__proveedores:
            print(f"RUC: {e.ruc}")
            print(f"RAZON: {e.razon}")
            print(f"CATEGORIA: {e.categoria}")
            print(f"DIRECCION: {e.direccion}")
            print(f"TELEFONO: {e.telefono}")
            print("-"*30)
            

class Producto:
    def __init__(self, idProducto,  nombre, tipo):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__tipo = tipo
    
    @property
    def idProducto(self):
        return self.__idProducto
    @property
    def nombre(self):
        return self.__nombre
    @property
    def tipo(self):
        return self.__tipo
    
    def mostrar_producto(self):
        print(f"Id producto: {self.__idProducto}")
        print(f"Nombre: {self.__nombre}")
        print(f"Tipo: {self.__tipo}")
        
                    
class Proveedores:
    def __init__(self, ruc,  razon, categoria, direccion, telefono):
        self.__ruc = ruc
        self.__razon = razon
        self.__categoria = categoria
        self.__direccion = direccion
        self.__telefono = telefono
    
    @property
    def ruc(self):
        return self.__ruc
    @property
    def razon(self):
        return self.__razon
    @property
    def categoria(self):
        return self.__categoria
    @property
    def direccion(self):
        return self.__direccion
    @property
    def telefono(self):
        return self.__telefono
    
def menu():
    print("MENU".center(30))
    print("-"*30)
    print("1. Insertar producto")
    print("2. Insertar proveedor")
    print("3. Modificar producto")
    print("4. Eliminar productos vencidos")
    print("5. Reportes")
    print("6. Salir")
    print("-"*30)
    print()

def repotes():
    print("REPORTES".center(30))
    print("1. Productos")
    print("2. Proveedores")
    print("0. Salir")


almacen = Almacen()


def main():
    try:
        while True:
            menu()
            opcion = int(input("Ingresar opcion deseada: "))
            if opcion == 6:
                break
            elif opcion == 1:
                print("-"*30)
                print("INGRESAR PRODUCTO".center(30))
                id = input("Introducir el id del producto: ")
                if id.isdigit():
                    nombre = input("Introducir el Nombre del producto: ")
                    if nombre.isalpha():
                        tipo = input("Introducir el TIpo del producto (polvo o liquido): ")
                        if tipo == "polvo" or tipo == "liquido":
                            objeto = Producto(id, nombre, tipo)
                            almacen.agregar_producto(objeto)
            elif opcion ==2:
                print("-"*30)
                print("INGRESAR PROVEEDOR".center(30))
                ruc = input("Introducir RUC: ")
                razon = input("Introducir Razon Social: ")
                if razon.isalpha():
                    categoria = input("Introducir Categoria (a,b,c): ")
                    categoria.upper()
                    if categoria == "A" or categoria == "B" or categoria == "C":
                        direccion = input("Ingresar la direccion: ")
                        if direccion.isalpha():
                            telefono = input("Ingresar el telefono: ")
                            if telefono.isdigit():
                                objeto = Proveedores(ruc, razon, categoria, direccion, telefono)
                                almacen.agregar_provedor(objeto)
            
            elif opcion == 5:
                while True:
                    repotes()
                    opcion = int(input("INGRESAR OPCION: "))
                    if opcion == 0:
                        break
                    elif opcion == 1:
                        almacen.listar_productos()
                    elif opcion == 2:
                        almacen.listar_proveedores()
        
    except ValueError:
        print("Error")

    
main()