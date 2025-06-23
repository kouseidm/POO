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
        if len(self.__productos) == 0:
            print("-"*30)
            print("NO HAY PRODUCTOS")
            print("-"*30)
        else:
            print("-"*30)
            print("LISTADO DE PRODUCTOS".center(30))
            print("-"*30)
            for e in self.__productos:
                print(f"ID PRODUCTO: {e.idProducto}")
                print(f"NOMBRE: {e.nombre}")
                print(f"TIPO: {e.tipo}")
                print(f"CANTIDAD: {e.cantidad}")
                print(f"CATEGORIA: {e.categoria}")
                print(f"AÑO: {e.año}")
                print(f"PRECIO: {e.precio}")
                print(f"PROVEEDOR: {e.proveedor}")
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
            
    def buscar_proveedor(self, ruc):
        for e in self.__proveedores:
            if e.ruc == ruc:
                return 1
        return 0
    
    def buscar_producto(self, producto):
        for e in self.__productos:
            if e.idProducto == producto:
                return 1
        return 0
    

    def modificar_producto(self):
        print("MODIFICAR PRODUCTO".center(30))
        print("-"*30)
        id = input("Ingresar id a cambiar: ")
        for e in self.__productos:
            if self.buscar_producto(id) == 1:
                break
            else:
                print("PRODUCTO NO REGISTRADO")
        while True:
            print("CAMBIAR: ")
            print("1. ID")
            print("2. Nombre")
            print("3. Tipo")
            print("4. Cantidad")
            print("5. Salir")
            opcion = int(input("Introducir opcion: "))
            if opcion == 5:
                break
            elif opcion == 1:
                id_cambio = input("Introducir nuevo id: ")
                if id_cambio.isdigit():
                    for e in self.__productos:
                        if e.idProducto == id:
                            e.idProducto = id_cambio
                else:
                    print("EL ID DEBEN SER NUMEROS")
            elif opcion == 2:
                nombre_cambio = input("Introoducir nuevo nombre: ")
                for e in self.__productos:
                        if e.idProducto == id:
                            e.nombre = nombre_cambio
                            break
    
    def mostrar_A_Natura(self):
        for e in self.__productos:
            if e.categoria == 'A' and e.proveedor == 'Natura':
                e.mostrar_producto()
    
    def eliminar_productos(self):
        proveedor_eliminar = input("Ingresar proveedor a eliminar productos: ")
        for e in self.__productos:
            if e.proveedor == proveedor_eliminar:
                self.__productos.remove(e)
        
        print("-"*30)
        print("PROUCTOS ELIMINADOS")
        print("-"*30)
        
    def eliminar_vencidos(self):
        cont = 0
        for e in self.__productos:
            if e.año != "2025":
                self.__productos.remove(e)
                cont += 1
        
        print("-"*30)
        print(f"Se eliminarion {cont} productos vencidos")
        print("-"*30)
            
        
            

class Producto:
    def __init__(self, idProducto,  nombre, tipo, cantidad, categoria, año, precio, proveedor):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__categoria = categoria
        self.__año = año
        self.__precio = precio
        self.__proveedor = proveedor
    
    @property
    def idProducto(self):
        return self.__idProducto
    @idProducto.setter
    def idProducto(self, id):
        self.__idProducto = id
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad (self, cantidad):
        self.__cantidad = cantidad
    
    @property
    def categoria(self):
        return self.__categoria
    @property
    def año(self):
        return self.__año
    @property
    def precio(self):
        return self.__precio
    @property
    def proveedor(self):
        return self.__proveedor
    
    
    
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
    print("3. Categorias A y Natura")
    print("4. Eliminar todos los productos de provedor x")
    print("5. Eliminar vencidos")
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
                            cantidad = input("Introducir cantidad: ")
                            if cantidad.isdigit():
                                while True:
                                    categoria = input("Introducir categoria: ")
                                    if categoria in ['A', 'B', 'C']:
                                        break
                                    else:
                                        print("Categoria [A,B,C]")
                                while True:
                                    año = input("Introducir año: ")
                                    if len(año) == 4:
                                        break
                                    else:
                                        print("Año incorrecto")
                                while True:
                                    precio = float(input("Introducir precio: "))
                                    if precio > 0:
                                        break
                                    else:
                                        print("mayor a 0")
                                while True:
                                    ruc = input("Intrudir el ruc del proveedor: ")
                                    if almacen.buscar_proveedor(ruc) == 1:
                                        objeto = Producto(id, nombre, tipo, cantidad, categoria, año, precio, ruc)
                                        almacen.agregar_producto(objeto)
                                        break
                                    else:
                                        print("REGISTRAR ANTES EL PROVEEDOR")      
                                                               
                                    
                            
                            
            elif opcion ==2:
                print("-"*30)
                print("INGRESAR PROVEEDOR".center(30))
                ruc = input("Introducir RUC: ")
                razon = input("Introducir Razon Social: ")
                if razon.isalpha():
                    categoria = input("Introducir Categoria (a,b,c): ").upper()
                    if categoria == "A" or categoria == "B" or categoria == "C":
                        direccion = input("Ingresar la direccion: ")
                        if direccion.isalpha():
                            telefono = input("Ingresar el telefono: ")
                            if telefono.isdigit():
                                objeto = Proveedores(ruc, razon, categoria, direccion, telefono)
                                almacen.agregar_provedor(objeto)
                                
            elif opcion == 3:
                almacen.modificar_producto()
            
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
                    elif opcion == 3:
                        almacen.mostrar_A_Natura()
                    elif opcion == 4:
                        almacen.eliminar_productos()
                    elif opcion == 5:
                        almacen.eliminar_vencidos()
        
    except ValueError:
        print("Error")

main()