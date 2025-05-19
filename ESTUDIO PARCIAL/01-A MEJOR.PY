lista_estudiantes = {}

def guardar_estudiante (codigo, datos):
    lista_estudiantes[codigo] =  datos
    
        
def registrar_estudiante ():
    print("REGISTRAR ESTUDIANTE")
    cod = input("Codigo del alumno: ")
    if (cod[0] == 'A' and cod[1:].isdigit() == True and len(cod) == 5):
        print("Continuando...")
        nombre = input("Nombre del estudiante: ")
        apellido_P = input("Apellido Paterno del estudiante: ")
        apellido_M = input("Apellido Materno del estudiante: ")
        if (nombre.isalpha() and apellido_M.isalpha() and apellido_P.isalpha()):
            print("Continuando...")
            edad = int(input("Ingresar edad"))
            if (edad > 0 and edad < 80):
                nota_t = int(input("Nota del trabajo: "))
                nota_e = int(input("Nota del Examen: "))
                nota_p = int(input("Nota de participacion: "))
                if (0<nota_t<=20 and 0<nota_e<=20 and 0<nota_p<=20):
                    notaF = (nota_p + nota_e + nota_t)/3
                    datos = [nombre,apellido_P,apellido_M,edad,nota_t, nota_e,nota_p,notaF]
                    guardar_estudiante(cod,datos)
                    
                else:
                    print("NOTAS ERROR")
            else:
                print("EDAD ERROR")
        else:
            print("NOMBRES ERROR")
    else:
        print("CODIGO MAL")    

def listado():
    print("N.\tCODIGO\t\tESTUDIANTE\t\t\tNOTA")
    for i, (codigo,datos) in enumerate(lista_estudiantes.items(), start=1):
        nombreCompleto = f"{datos[0]} {datos[1]} {datos[2]}"
        print(f"{i}.\t{codigo}\t\t{nombreCompleto}\t\t{datos[7]}")

def actualizar():
    cod = input("Codigo del alumno: ")
    if (cod[0] == 'A' and cod[1:].isdigit() == True and len(cod) == 5):
        for (cod1, datos) in lista_estudiantes.items():
            if cod == cod1:
                nota_t = int(input("Nota del trabajo cambiar: "))
                nota_e = int(input("Nota del Examen cambiar: "))
                nota_p = int(input("Nota de participacion cambiar: "))
                if (0<nota_t<=20 and 0<nota_e<=20 and 0<nota_p<=20):
                    notaF = (nota_p + nota_e + nota_t)/3
                    datos[4] = nota_t
                    datos[5] = nota_e
                    datos[6] = nota_p
                    datos[7] = notaF
                else:
                    print("Error de notas")
            else:
                print("no encontrado")
    else:
        print("No encontrado")
def buscar():
    cod = input("Codigo del alumno: ")
    if (cod[0] == 'A' and cod[1:].isdigit() == True and len(cod) == 5):
        for (cod1,datos) in lista_estudiantes.items():
            if cod == cod1:
                nombreCompleto = f"{datos[0]} {datos[1]} {datos[2]}"
                print("DATOS DEL ALUMNO")
                print("-"*30)
                print(f"Codigo: {cod1}")
                print(f"Nombre: {nombreCompleto}")
                print(f"Edad: {datos[3]}")
                print(f"Nota final: {datos[7]}")

def eliminar():
    cod = input("Codigo del alumno: ")
    if cod in lista_estudiantes:
        lista_estudiantes.pop(cod)


def obtener_nota_F(item):
    return item[1][7]

def descendente():
    lista_ordenada = sorted(lista_estudiantes.items(), key=obtener_nota_F, reverse=True)
    for i, (cod, datos) in enumerate(lista_ordenada,start=1):
        print(f"{i}:COD {cod}, Nombre {datos[0]}, Nota {datos[7]}")
        

def menu():
    print("BIENVENIDOS")
    print("1. Registrar")
    print("2. Actualizar")
    print("3. Buscar")
    print("4. Listado")
    print("6. Listado orden descendente")
    print("7. Eliminar")
    print("5. Salir")

def main():
    try:
        while True:
            menu()
            opcion = int(input("OPCION: "))
            if opcion == 5:
                break
            elif opcion == 1:
                registrar_estudiante()
            elif opcion == 2:
                actualizar()
            elif opcion == 3:
                buscar()
            elif opcion == 4:
                listado()
            elif opcion == 6:
                descendente()
            elif opcion == 7:
                eliminar()
            else:
                print("ERROR DE OPCION") 
    except ValueError:
        print("ERROR")
main()
