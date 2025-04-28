def menu ():
    print ("\n")
    print ("MENU")
    print ("---------------------")
    print ("1. Añadir/modificar")
    print ("2. Buscar")
    print ("3. Borrar")
    print ("4. Listar")
    print ("5. Salir")

agenda = {}
while True:
    menu()
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        nombre = input ("Ingrese nombre: ")
        if nombre in agenda:
            print ("%s ya existe y su telefono es %s" % nombre, agenda[nombre])
            opcion = input("Presiona s si quieres modificar. Otra tecla para continuar")
            if opcion == "s":
                numero = input ("Ingrese nuevo numero de telefono: ")
                agenda[nombre] = numero
        else:
            numero = input("Ingrese el numero: ")
            agenda[nombre] = numero
    elif opcion == 2:
        cadena = input ("Nombre de persona a buscar: ")
        for nombre,numero in agenda.items():
            if nombre.startswith(cadena):
                print ("el numero de telefono de %s es el %s ", (nombre,agenda[nombre]))
    elif opcion == 3:
        nombre = input ("Nombre de la persona a borrar: ")
        if nombre in agenda:
            opcion = "Presiona s si quieres borrar. Otra tecla para continuar"
            if opcion == "s":
                del agenda[nombre]
        else: 
            print ("No existe la persona. ")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print (nombre, "->", numero)
    elif opcion == 5:
        break
    else:
        print("OPCION INCORRECTA. ")