try:
    while True:
        num = int(input("Ingrese un numero entero mayor a cero: "))
        if num > 0:
            if num % 2 == 0:
                mitad = num // 2
                print ("NUMERO PAR")
                print("EL numero", num , "es el dobre de ", mitad)
            else:
                y = num / 2
                print ("NUMERO IMPAR")
                print ("El numero", num, "es el doble de un impar", y) 
        else:
            print("El numero debe ser mayor a 0")   
    
except ValueError:
    print("El valor debe ser un numero entero.")