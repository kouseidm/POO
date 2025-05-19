lista_estudiantes = []
def guardar_estudiante(cod, nombre, apellido_p, apellido_m, edad, nota_trabajo, nota_examen, part, Nota_Final):
    guardar = {
        "cod": cod,
        "nombre": nombre,
        "paterno": apellido_p,
        "materno":apellido_m,
        "edad":edad,
        "n.trabajo": nota_trabajo,
        "n.examen": nota_examen,
        "part" : part,
        "notaF": Nota_Final
    }
    lista_estudiantes.append(guardar)    
def mostrar_estudiantes():
    if not lista_estudiantes:
        print("No hay estudiantes")
    else:
        for i, estudiantes in enumerate(lista_estudiantes , start=1):
            print(f"{i}: Codigo: {estudiantes['cod']}, NotaFinal: {estudiantes['notaF']}")

def actualizar_notas():
    try:
        codigo = input("Ingrese el codigo del alumno: ")
        encontrado = False
        for estudiante in lista_estudiantes:
            if codigo == estudiante["cod"]:
                encontrado = True
                nota_trabajo = int(input("Nota del trabajo: "))
                nota_examen = int(input("Nota del examen: "))
                part = int(input("Nota de participacion: "))
                Nota_Final = (nota_trabajo+nota_examen+part)/3
                #------------------------
                estudiante["n.trabajo"] = nota_trabajo
                estudiante["n.examen"] = nota_examen
                estudiante["part"] = part
                estudiante["notaF"] = Nota_Final
                print("Notas actualizadas")
                break
        if encontrado == False:
            print("No encontrado")
    except ValueError:
        print("Error")

def buscar_alumno():
    try:
        codigo = input("ingresar el codigo")
        encontrado = False
        for estudiante in lista_estudiantes:
            if codigo == estudiante["cod"]:
                encontrado = True
                print("Estudiante Encontrado")
                print(f"==============Datos==============")
                print(f"Codigo: {estudiante["cod"]}")
                print(f"Nombre: {estudiante["nombre"]}")
                print(f"Apellido Paterno: {estudiante["paterno"]}")
                print(f"Apellido Materno: {estudiante["materno"]}")
                print(f"Edad: {estudiante["edad"]}")
                print(f"Nota Final: {estudiante["notaF"]}")
        if encontrado == False:
            print("No encontrado")
    except ValueError:
        print("Error")

def ordenar_alumno():
    print("LISTADO DE ALUMNOS EN ORDEN DESCENDENTE POR NOTA FINAL")
    lista_ordenada = sorted(lista_estudiantes, key=lambda x:x["notaF"], reverse=True)
    for i, estudiante in enumerate(lista_ordenada, start=1):
        print(f"{i}: cod {estudiante["cod"]}, nombre {estudiante["nombre"]}, notaF {estudiante["notaF"]}")
    
    
def menu():
    print("BIENVENIDO")
    print("1. Registrar alumnos")
    print("2. Modificar notas")
    print("3. Buscar alumno")
    print("4. Listaodde alumnos en orden descendente")
    print("5. Salir")

def main():
    try:
        while True:
            menu()
            opcion = int(input("Ingresar opcion: "))
            if opcion == 5:
                break
            elif opcion == 1:
                print("REGISTRAR ALUMNO")
                cod = input("Codigo (AXXXX): ")
                nombre = input("Nombre: ")
                apellido_p = input("Apellido P: ")
                apellido_m = input("Apellido M: ")
                edad = input("Edad: ")
                nota_trabajo = int(input("nota trabajo: "))
                nota_examen = int(input("nota examen: "))
                nota_participacion = int(input("nota participacion: "))
                notaF = (int(nota_examen) + int(nota_participacion) + int(nota_trabajo))/3
                if not (len(cod) == 5 and cod[0] == 'A' and  cod[1:].isdigit()):
                    print("Error codigo")
                elif not (nombre.isalpha()):
                    print("Error nombre")
                elif not (apellido_p.isalpha()):
                    print("Error ape")
                elif not (apellido_m.isalpha()):
                    print("Error aope")
                elif not (20 >= nota_examen >= 0 and 20 >= nota_participacion >= 0 and 20 >= nota_trabajo >= 0 ):
                    print ("Error de notas")
                else:
                    guardar_estudiante(cod, nombre, apellido_p, apellido_m, edad, nota_trabajo, nota_examen, nota_participacion, notaF)
                    mostrar_estudiantes()
            elif opcion == 2:
                actualizar_notas()
            elif opcion == 3:
                buscar_alumno()
            elif opcion == 4:
                ordenar_alumno()
            else:
                print("Error de opcion") 
                    
    except ValueError:
        print("Error")    
main()