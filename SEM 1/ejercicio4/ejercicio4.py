try:
    seg = int(input("Ingrese la cantidad de segundos: "))

    horas = seg // 3600
    aux = seg % 3600
    

    minutos = aux // 60
    segundos = aux % 60

    print("Horas = ", horas)
    print("Minutos = ", minutos)
    print("Segundos = ", segundos)

except ValueError:
    print("Error, el valor ingresado no es entero")

