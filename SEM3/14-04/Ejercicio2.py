
lista=[]
print ("El programa termina al ingresar un 0")
while True:
    num= int(input("Ingresar el numero: "))
    if num > 0:
        lista.append(num)
    else: 
        print("Debe ser un numero diferente a 0")
        break
        
print (len (lista))
print (lista[-1])
print (lista[::-1])
