
class cliente:
    def __init__(self, dni, nombre, direc, telef, correo, preferente):
        self.dni = dni
        self.nombre = nombre
        self.direc = direc
        self.telef = telef
        self.correo = correo
        self.preferente = preferente
        
    def vercliente(self):
        print("<<< CLIENTE >>>".center(10))
        print(f"Dni = {self.dni}")
        print(f"Nombre = {self.nombre}")
        print(f"Direc = {self.direc}")
        print(f"Telef = {self.telef}")
        print(f"Correo = {self.correo}")
        print(f"Preferencia = {self.preferente}")
    
class baseClientes:
    def __init__(self):
        self.listaClientes = []
    def registrar(self, dni, nombre, direc, telef, correo, preferente):
        clienteN = cliente(dni, nombre, direc, telef, correo, preferente)
        self.listaClientes.append(clienteN)
        return clienteN
    def actualizar(self, dni, nombre, direc, telef, correo, preferente):
        print("aaaaaaaaaaaaa")
"""
def main():
    while True:
        opcion = int(input("Ingresar opcion: "))
        if opcion == 1:
            print("A")

"""