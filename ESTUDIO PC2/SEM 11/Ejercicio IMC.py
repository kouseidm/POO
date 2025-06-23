
from random import randint

class Hospital:
    def __init__ (self):
        self.__lista = []
    
    def agregar_persona(self, objeto):
        self.__lista.append(objeto)
        print("PERSONA AGREGADA AL HOSPITAL")
    
    def listar(self):
        print("DATOS: ")
        for e in self.__lista:
            print(f"Nombre: {e.nombre}")
            print(f"Edad: {e.edad}")
            print(f"Dni: {e.dnu}")
            print(f"Sexo: {e.sexo}")
            print(f"Peso: {e.peso}")
            print(f"Altura: {e.altura}")
    
class Persona:
    def __init__(self, nombre= "", edad= 0, peso=0, altura=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = self.generar_dni()
        self.__sexo = "F"
        self.__peso = peso
        self.__altura = altura
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad (self,edad):
        self.__edad = edad
    
    @property
    def dni(self):
        return self.__dni

    @property
    def sexo(self):
        return self.__sexo

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    def generar_dni(self):
        b = randint(1000000, 9999999)
        a = randint(0,9)
        dni = str(a) + str(b)
        return dni
    
    def calcularIMC(self):
        IMC = (self.peso/(self.altura**2 ))
        IMC = round(IMC, 2)
        return IMC

    def valorarPesoCorporal(self):
        if self.calcularIMC() > 25:
            return 1
        elif self.calcularIMC() <18:
            return -1
        else:
            return 0
    
    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    def __str__(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Dni: {self.dni}")
        print(f"Sexo: {self.sexo}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")

    
    
    
def menu():
    print("BIENVENIDO".center(30))
    print("-"*30)
    print("1. Registrar")
    print("2. Calcular IMC")
    print("3. valorPesoCorpotal")
    print("4. Es mayor de edad?")
    print("5. Generar DNI")
    print("6. Listado")
    print("0. Salir")
    print("-"*30)


def main():
    try:
        objeto = 0
        while True:
            menu()
            opcion = int(input("INGRESAR OPCION: "))
            print("-"*30)
            if opcion == 0:
                break
            elif opcion == 1:
                while True:
                    nombre = input("Ingresar nombre: ")
                    if nombre.isalpha():
                        break
                    else:
                        print("El nombre debe ser digitos")
                while True:
                    edad = int(input("Ingresar edad: "))
                    if edad > 0 and edad < 90:
                        break
                    else:
                        print("Edad entre 0 y 90")
                while True:
                    peso = float(input("Introducir peso: "))
                    if peso > 0:
                        break
                    else: 
                        print("Peso mayor a 0")
                while True:
                    altura = float(input("Introducir altura: "))
                    if altura > 0:
                        break
                    else: 
                        print("Altura mayor a 0")
                objeto = Persona(nombre, edad, peso, altura)
                objeto2 = Persona(nombre,edad)
                objeto3 = Persona()
                
                #OBJETO3
                objeto3.nombre = "Ashly"
                objeto3.edad = 28
                objeto3.peso = 55
                objeto3.altura = 1.60
                
                print("PERSONA REGISTRADA")
            elif opcion == 2:
                print("-"*30)
                print("CALCULAR IMC: ")
                print("-"*30)
                print(f"IMC de {objeto.nombre}= {objeto.calcularIMC()}")
                print(f"IMC de {objeto3.nombre}= {objeto3.calcularIMC()}")
                print("-"*30)
            elif opcion == 3:
                print("-"*30)
                print("VALORAR PESO CORPORAL: ")
                print("-"*30)
                print("DATO: -1 = DEBAJO DEL PESO IDEAL")
                print("DATO: 0 = PESO IDEAL")
                print("DATO: 1 = SOBREPESO")
                print("-"*30)
                print({objeto.nombre}, objeto.valorarPesoCorporal())
                print({objeto3.nombre}, objeto3.valorarPesoCorporal())
                print("-"*30)
            elif opcion == 4:
                print("-"*30)
                print(f"{objeto.nombre} MAYOR DE EDAD: {objeto.esMayorDeEdad()}")
                print(f"{objeto3.nombre} MAYOR DE EDAD: {objeto3.esMayorDeEdad()}")
                print("-"*30)
            elif opcion == 5:
                print("-"*30)
                print(f"{objeto.nombre} DNI GENERADO: {objeto.dni}")
                print(f"{objeto3.nombre} DNI GENERADO: {objeto3.dni}")
                print("-"*30)
            elif opcion == 6:
                if objeto == 0:
                    print("AUN NO REGISTRADO")
                else:
                    print("-"*30)
                    print("LISTADO: ")
                    print("-"*30)
                    objeto.__str__()
                    print("-"*30)
                    objeto2.__str__()
                    print("-"*30)
                    objeto3.__str__()
                
                

            
    except ValueError:
        print("ERROR")
main()