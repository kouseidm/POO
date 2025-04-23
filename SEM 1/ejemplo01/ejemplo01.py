# ejemplo de python 31/03/25 SEM 1
""" print("Nombre:")
print("Luis Alberto")
print("Apellido:")
print("Rodrigez Vargas")
print("============") """
# en una sola linea                #end="/n"
print("Nombre:", end=" ")
print("Luis Alberto")
print("Apellido:", end=" ")
print("Rodrigez Vargas")
print("============")

print('Marte', 'Jupiter', 'Saturno') #sep=" "
print('Marte', 'Jupiter', 'Saturno', sep=', ', end=', ')
print('Urano', 'Neptuno', 'Pluton', sep=', ')

print('Separar varios argumentos', end='\n * ')
print('Prevencion de saltos de linea')
print("==============================")

x= "8" #
print(x)
print(type(x))
x = int(x)
print(x)
print(type(x))


try:
    x = int(input('Ingresa tu edad: '))
    print(x)
    print(type(x))
except :
    print("Error, no es un numero entero c:")

