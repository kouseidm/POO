from random import randint

lista = []
lista2= []
cont = 0
for i in range (50):
    num = randint(1,100)
    lista2.append (num)
    lista.append(num*2)   
    
for i in lista:
    if i >= 50:
        cont = cont + 1

print (f"La lista original: ", lista)
print (f"La lista doble: ", lista2)
print (f"Valores mayor a 50: ",cont)
