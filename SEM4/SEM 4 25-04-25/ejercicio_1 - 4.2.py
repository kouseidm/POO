alumnos = {}
cantidad = int(input("Ingrese la cantidad de alumnos: "))
for n in range(cantidad):
    nombre = input("Ingrese el nombre del alumno: ")
    while nombre in alumnos:
        print ("Alumno ya existente")
        nombre = input("Nombre del alumno: ")
    notas = []
    nota = int (input("Ingrese nota del alumno (negativo para fin): "))
    while nota >= 0:
        notas.append(nota)
        nota = int(input("Ingrese nota del alumno (negativo para fin): "))
    alumnos [nombre] = notas.copy()
for nombre, notas in alumnos.items():
    print ("%s ha optenido un promedio de %f" % (nombre, sum(notas)/len(notas)))
    