
try:
    while True:
        
        num = int(input("Ingrese el numero a analizar: "))
        if num > 0:
            num = str(num)
            print (num[::-1])
        else:
            print ("El valor debe ser positivo")
      
except ValueError:
    print("ingrese un valor real")
