class Edificio:
    def __init__(self, idEdificio, direccion, departamento, junta, admin):
        self.__idEdificio = idEdificio
        self.__direccion = direccion
        self.__departamentos = {}
        self.__junta = junta
        self.__admin = admin
        self.agregar(departamento)
        
        
    def agregar(self, departamentos):
        if isinstance(departamentos, Departamento):
            self.__departamentos[departamentos.idDepartamento] = departamentos
    @property
    def idEdificio (self):
        return self.__idEdificio
    @property
    def direccion (self):
        return self.__direccion

    def listar_edificio(self):
        print("Administrador: ")
        self.__admin.__str__()
        print("-"*30)
        print("Departamentos: ")
        print("-"*30)
        for e in self.__departamentos.values():
            print(f"ID: {e.idDepartamento}, Nro Habitaciones: {e.num}")
        print("-"*30)
        print("Junta de propietarios: ")
        self.__junta.listar_propietarios()
        
class Administrador:
    def __init__(self, idAdministrador, nombre):
        self.__idAdministrador = idAdministrador
        self.__nombre = nombre
    @property
    def idAdministrador (self):
        return self.__idAdministrador
    
    @property
    def nombre (self):
        return self.__nombre

    def __str__(self):
        print("-"*30)
        print(f"Id del Admin: {self.idAdministrador}")
        print(f"Nombre del Admin: {self.nombre}")
    
class JuntaPropietarios:
    def __init__(self, idJunta, fecha, propietarios):
        self.__idJunta = idJunta
        self.__fecha = fecha
        self.__propietarios = {}
        self.agregar(propietarios)
    
    def agregar(self, propietario):
        if isinstance(propietario, Propietarios):
            self.__propietarios[propietario.idPropietario] = propietario

    
    @property
    def idJunta (self):
        return self.__idJunta
    @property
    def fecha (self):
        return self.__fecha
    
    def listar_propietarios(self):
        print("-"*30)
        for e in self.__propietarios.values():
            print(f"Id: {e.idPropietario}, Nombre {e.nombre}")

class Propietarios:
    def __init__(self, idPropietario, nombre):
        self.__idPropietario = idPropietario
        self.__nombre = nombre
    @property
    def idPropietario (self):
        return self.__idPropietario
    @property
    def nombre (self):
        return self.__nombre
    def __str__(self):
        print("-"*30)
        print(f"Id del Propietario: {self.idPropietario}")
        print(f"Nombre del Propietario: {self.nombre}")
    
class Departamento:
    def __init__(self, idDepartamento, num):
        self.__idDepartamento = idDepartamento
        self.__num = num
    @property
    def idDepartamento (self):
        return self.__idDepartamento
    @property
    def num (self):
        return self.__num
    def __str__(self):
        print("-"*30)
        print(f"Id del Departamento: {self.idDepartamento}")
        print(f"Numero de habitaciones: {self.num}")

Admin = Administrador("60914417","Ashly")
depar1 = Departamento("u2021", 4)
depar2 = Departamento("u2023", 3)
depar3 = Departamento("u2024", 6)
propie1 = Propietarios("b750", "pepe")
propie2 = Propietarios("b540", "carlos")
propie3 = Propietarios("b120", "martin")

junta = JuntaPropietarios("abz", "19/02/2024", propie1)
junta.agregar(propie2)
junta.agregar(propie3)

edificio = Edificio("1","lima",depar1, junta, Admin)
edificio.agregar(depar2)
edificio.agregar(depar3)

edificio.listar_edificio()
