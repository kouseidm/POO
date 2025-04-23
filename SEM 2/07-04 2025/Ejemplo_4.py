try:
    while True:
        a=int(input("Ingresa el 1er valor: "))
        b=int(input("Ingresa el 2d valor: "))
        c=int(input("Ingresa el 3er valor: "))
        
        if a == b or a == c or b == c:
            print("Error, los numero ingresados deben ser diferentes")
        else:
            if a > b and a > c:
                mayor = a
            if b > a and b > c:
                mayor = b
            if c > a and c > b:
                mayor = c
            if a < b and a < c:
                menor = a
            if b < a and b < c:
                menor = b
            if c < a and c < b:
                menor = c
                
           
        
        print ("el mayor es:", mayor)
        print ("el menor es:", menor)
    
except ValueError:
    print ("Error, el valor debe sel un numero entero.")