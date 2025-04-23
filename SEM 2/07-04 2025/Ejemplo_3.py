try:
    while True:
        num = int(input("Ingrese un valor entero positivo: "))
        if 1 <= num <= 100:
            if 1 <= num <= 9:
                ndig = 1
            if 10 <= num <= 99:
                ndig = 2
            else:
                ndig = 3
            print ("El numero de digitos del numero es: ", ndig)
        else: 
            print("Error, el numero debe ser entero positivo entre 1 y 100.")    
except ValueError:
    print ("Error, el valor debe ser un numero")
