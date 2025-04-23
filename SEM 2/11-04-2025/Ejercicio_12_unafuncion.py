try:
    while True:
        a = int(input("Ingresar el primer numero entero positivo"))
        b = int(input("Ingresar el segundo numero entero positivo"))
        c = int(input("Ingresar el tercer numero entero positivo"))
        if a >= 0 and b>=0 and c >=0:
            
            mayor = 0
            if a>b and a>c:
                mayor = a
            elif b>a and b>c:
                mayor = b
            else:
                mayor = c

            menor = 0
            if a<b and a<c:
                menor = a
            elif b<a and b<c:
                menor = b
            else:
                menor = c   

            medio = a + b + c - mayor - menor


            print("orden descendente: ", mayor, medio, menor)
            
        else :
            print ("Todos los valores deben ser enteros positivos")

except ValueError:
    print ("Todos los valores deben ser enteros positivos.")