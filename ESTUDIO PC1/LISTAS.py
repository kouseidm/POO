lista = [] 
# LA LISTA ES UNA COLLECCION ORDENADA Y MODIFICABLE DE ELEMENTOS, PERMITE DUPLICADOS
# LOS ELEMENTOS PUEDEN SER CUALQUIER ELEMENTO:  str, int, float, string, lista, bool
# PUEDEN HABER LISTAS DENTRO DE OTRA LISTA, TUPLAS, DICCIONARIOS, ETC

resumen = dict()
texto = list()

# POSICION DE LOS ELEMENTOS EN UNA LISTA
lista = ["Alberto", "Juan", "Mario", "Renan", "Luis", "Javier", "Humberto"]
print(lista[2:4])
print(lista[-2])
print(lista[::-1])
# print(lista[0 = INICIO :5 = FINAL :2 = SALTOS])

# AÑADIR ELEMENTOS A UNA LISTA
lista.append("Alexis")
print(lista)

# MODIFICAR UNA LISTA
lista[7] = "MIGUEL"
print(lista)

# ELIMINAR ELEMENTOS DE UNA LISTA
lista.pop() # ELIMINA EL ULTIMO ELEMENTO DE LA LISTA
print(lista)

lista = ["Alberto", "Juan", "Mario", "Renan", "Luis", "Javier", "Humberto"]
lista2 = []
lista2 = lista.copy()
print (id(lista))
print (id(lista2))
print (lista)
print (lista2)


