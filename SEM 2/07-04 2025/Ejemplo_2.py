try:
    while True:
        gradosf =float(input("Escriba la temperatura en grados Fahrenheit: "))
        if gradosf >= -459.67:
            break
    gradosc= (gradosf-32)/1.8
    print("Angulo en grados sexagesimales =", gradosc)
except ValueError:
    print("El valor debe ser real.")
        
        
#el TRY sirve para que en el programa no permita ingresar letras.

