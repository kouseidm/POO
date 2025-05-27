class Grifo:
    def __init__(self, nombre):
        self.__nombre = nombre
    def cargarCombustible(self, cantidad):
        print(f"Cargando {cantidad} litros de combustible en "
            f"{self.__nombre}..." 
            )
        
class Coche:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__combustible = 0
    def conducir(self, distancia):
        if self.__combustible >= distancia * 0.1:
            print(f"Conduciendo {distancia} km en un "
                 f"{self.__marca} {self.__modelo}..."
                 )
            self.__combustible -= distancia * 0.1
        else:
            print(f"No hay suficiente combustible para conducir "
                f"{distancia} km."
                )
    def cargarEnGrifo(self, grifo, cantidad):
        grifo.cargarCombustible(cantidad)
        self.__combustible += cantidad
        print(
        f"El {self.__marca} {self.__modelo} ahora tiene "
        f"{self.__combustible} litros de combustible."
        )
    def mostrarDetalles(self):
        print(
        f"Coche: {self.__marca} {self.__modelo}, "
        f"Combustible: {self.__combustible} litros"
        )

# Programa Principal
miGrifo = Grifo("Grifo 24 Horas")
miCoche = Coche("Nissan", "Sentra")
# Uso de la dependencia
miCoche.mostrarDetalles()
miCoche.cargarEnGrifo(miGrifo, 30)
miCoche.conducir(100)
miCoche.conducir(400)
miCoche.mostrarDetalles()