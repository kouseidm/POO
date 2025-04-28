tupla = ()
# son immutables, no se pueden modificar
# son iterables, se pueden recorrer
# cualquier tipo de dato puede estar dentro de una tupla

a = 125
b = 3.14159
c = "Ana"
d = a, b, c
print(type(d))
print(d)
print(len(d)) # len también funciona en tuplas 

# Ejemplo de desempaquetado de tuplas
t = 125, 3.14159, "Ana"
x, y, z = t
print(x, y, z)

