print("Hallar el resultado de x^4 + x^3 + 2x^2 -x + 11")
try:
    x = float(input('Ingresar el valor de x: '))
    r = x**4 + x**3 + 2*x**2 - x+11

    print("El resultado es: ", r)
except ValueError:
    print("El valor no es un numero")


#EJERCICIO 2
print("_________________________________________________")
print ("Hallar el resultado de 13x^3 + 1/2x^1/2 -x + 3.")
try:
    x = float(input('Ingresar el valor de x: '))
    r = 13*x**3 + 0.5*(x**0.5) -x + 3

    print("El resultado es: ", r)
except ValueError:
    print("El valor no es un numero")


#EJERCICIO 3
print("_________________________________________________")
print("Hallar los resultados de :")
try:
    a = float(input('Ingresar el valor de A: '))
    b = float(input('Ingresar el valor de B: '))
    c = float(input('Ingresar el valor de C: '))
    resA = ((b * b) - (4 * a * c)) / (2 * a)
    resB = (b * b - 4 * a * c) / (2 * a)
    resC = b * b - 4 * a * c / 2 * a
    resD = (b * b) - (4 * a * c / 2 * a)
    resE = 1 / 2 * b
    resF = b / 2

    print("El resultado del ejercicio A: ", resA)
    print("El resultado del ejercicio B: ", resB)
    print("El resultado del ejercicio C: ", resC)
    print("El resultado del ejercicio D: ", resD)
    print("El resultado del ejercicio E: ", resE)
    print("El resultado del ejercicio F: ", resF)

except ValueError:
    print("El valor no es un numero")
