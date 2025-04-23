lista=[]
cont_p = 0
cont_n = 0

print ("El programa termina al ingresar un 0")
while True:
    
    num= int(input("Ingresar el numero: "))
    if num != 0:
        lista.append(num)
    else: 
        break
   
    for i in lista:
        if lista[::i] >= 1:
            cont_p = cont_p +1 
        elif lista[i] <= -1:
            cont_n =cont_n+1
#     for i in lista:
#         suma = suma + i
             
# promedio = suma / len(lista)

print ("Numero leidos: ", len (lista))
print ("Cantidad de numeros positivos: ", cont_p)
print (f"Cantidad de numeros negativos: {cont_n}")
# print (f"El promedio de la lista es: {promedio}")
print (lista[::-1])
