listas = []
tuple = ()
dicc = {}  # CLAVE: VALOR

# DICCIONARIOS
# EL DICCOIONARIO NO PERMITE ELEMENTOS DUPLICADOS, NO SON ORDENADOS Y SON MUTABLES
# CKAVES SOLO PUEDEN SER pueden ser strings, enteros, flotantes, TUPLAS
# VALORES PUEDEN SER CUALQUIER TIPO DE DATO (LISTAS, TUPLAS, DICCIONARIOS, ETC)
dicc = {
    2 : "Ashly",
    "Pedro" : 3,
    3.2 : 4,
    5 : (1,3,4)
    }

print (dicc)
print (dicc[2]) # acceder al valor de la clave 2
print (len(dicc)) # valores del diccionario
print (dicc[5][::-1]) # invertir la tupla

#AÑADIR DATOS:
dicc[1] = "pepe"   # añadir un nuevo elemento al diccionario
dicc["antony"] = 1 
print (dicc)

lista1 = list(dicc.values())  #mostrar los valores -> derecha del diccionario
print (lista1)

lista2 = list(dicc.keys()) # mostrar las claves -> izquierda del diccionario
print (lista2)

lista3 = list(dicc.items()) #mostrar las claves y valores -> izquierda y derecha del diccionario
print (lista3)
print ()
print ("----------------------------------------------")
print ()

auto = {
"marca": "Ford",
"modelo": "Mustang",
"año": 1964,
"colores": ["rojo", "azul", "negro"],
}
for llaves in auto:
    print(f"{llaves}")
print()
for i in auto.keys():
    print(f"{i}")
print()
for valores in auto.values():
    print(f"{valores}")
print()
for llaves, valores in auto.items():
    print(f"{llaves} {valores}")

print ()
print ("----------------------------------------------")
print ()

# get 
recuentos = dict()
nombres = {'csev', 'cwen', 'csev', 'zqian', 'cwen'}
for nombre in nombres:
    recuentos[nombre] = recuentos.get(nombre, 0) +1  # el método get() es para contar (x,0) + 1, si no existe devuelve 0
print(recuentos)

# la función split() crea una lista con las palabras del texto
texto = """
el payaso corrió detrás del coche y el coche se metió en la tienda y
la tienda cayó sobre el payaso y el coche
"""
recuento = dict()
palabras = texto.split() # la función split() crea una lista con las palabras del texto
print("Palabras:", palabras)
print("\nContando...")
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print('Recuento', recuento)

print ()
print ("----------------------------------------------")
print ()

# ELIMINAR ELEMENTOS DE UN DICCIONARIO
palabras = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
}

palabras.pop("A")  # eliminar el elemento "A" del diccionario
print(palabras) 

# AÑADIR ELEMENTOS A UN DICCIONARIO O JUNTAR DICCIONARIOS
palabras2 = {
    "L": 1,
    "K": 2,
    "H": 3,
    "N": 4,
}
palabras.update({"Z": 123})
palabras.update(palabras2)# añadir el elemento "A" al diccionario
print(palabras) 