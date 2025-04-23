from random import randint
while True:
    try:
        elem = int (input("Número de elementos: "))
        if elem > 0 and elem < 51:
            break
        else:
            print ("El valor debe ser ente 0 y 50")
        
    except ValueError:
        print ("El valor debe ser un numero real")
        
lista = []      
for i in range(elem):
    lista.append(randint(1,100))
    
print(lista)

#Imprima en cada línea secuencias de números ascendentes que se encuentren en la lista.
for i in range(elem-1):
    if lista[i] < lista [i+1]:
        print(lista[i], end=" ")
    else:
        print(lista[i])
print (lista[elem-1])
        
    
    