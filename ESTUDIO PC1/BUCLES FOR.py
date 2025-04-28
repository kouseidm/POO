# bucles con for
# for recorre los elementos de una secuencia (lista, tupla, cadena, diccionario, conjunto)
# for variable in rango:
holaMundo = "Hola, mundo."
for caracter in holaMundo:
    print(caracter)

# BUSACAR UN CARACTER EN UNA CADENA
x = "Curso Progamación Orientada a Objetos"
if "P" in x:
    print("Correcto")
else:
    print("Errado")
    
# ENUMERATE()
# en vez de crear una variable que cuente, se puede usar enumerate() que devuelve un objeto enumerado, que contiene una secuencia de tuplas (índice, valor)
# enumerate(iterable, inicio=0)
cadena = "Hola mundo"
for i, valor in enumerate(cadena):
    print(i, valor)
for i, valor in enumerate(cadena, 1):
    print(i, valor)


# APENDIENDO SE USA PARA AÑADIR UN ELEMENTO AL FINAL DE UNA LISTA
colores = ["azul", "blanco", "negro"]
nuevo_color = "marrón"
if nuevo_color in colores:
    print("Elemento ya existe en la lista")
else:
    colores.append(nuevo_color)
print(colores)

holaMundo = "Hola, mundo."
print(len(holaMundo))
for i in range(len(holaMundo)):
    print(holaMundo[i]) # imprime cada caracter de la cadena
    
lista1 = list(range(2, 12, 2))
print(lista1) # imprime una lista de números del 2 al 12 de 2 en 2