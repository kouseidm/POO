
# type = MUESTRA EL TIPO DE DATO DEL VALOR
# len = MUESTRA LA LONGITUD DEL VALOR
# string.find(valor, inicio, final*) = BUSCA UN VALOR EN UNA CADENA Y DEVUELVE LA POSICION DEL VALOR BUSCADO, SI NO ENCUENTRA NADA DEVUELVE -1
# string.isdigit() = DEVUELVE TRUE SI LA CADENA SOLO CONTIENE DIGITOS, FALSE SI NO
# string.lower() = DEVUELVE LA CADENA EN MINUSCULAS
# string.upper() = DEVUELVE LA CADENA EN MAYUSCULAS
# string.replace(antiguo, nuevo, contador) = REEMPLAZA UN VALOR POR OTRO EN UNA CADENA, SI NO SE ESPECIFICA EL CONTADOR REEMPLAZA TODOS LOS VALORES
# string.strip(caracteres) = ELIMINA LOS ESPACIOS EN BLANCO AL INICIO Y AL FINAL DE UNA CADENA, SI SE ESPECIFICA UN CARACTER ELIMINA ESE CARACTER
# string.title() = DEVUELVE LA CADENA CON LA PRIMERA LETRA DE CADA PALABRA EN MAYUSCULAS
# string.capitalize() = DEVUELVE LA CADENA CON LA PRIMERA LETRA EN MAYUSCULAS Y EL RESTO EN MINUSCULAS
# variable.count(valor) = DEVUELVE EL NÚMERO DE VECES QUE APARECE UN VALOR EN UNA CADENA
# max() = DEVUELVE EL VALOR MAXIMO DE UNA LISTA O TUPLA
# min() = DEVUELVE EL VALOR MINIMO DE UNA LISTA O TUPLA
# sum() = DEVUELVE LA SUMA DE LOS VALORES DE UNA LISTA O TUPLA
# String_separador.join(iterable) = UNE LOS ELEMENTOS DE UNA LISTA O TUPLA EN UNA CADENA, SEPARADOS POR EL SEPARADOR ESPECIFICADO
# sorted(iterable, key=Func*, reverse=True/False) = ORDENA LOS ELEMENTOS DE UNA LISTA O TUPLA, SI SE ESPECIFICA LA FUNCION KEY SE ORDENA POR EL VALOR DEVUELTO POR LA FUNCION, SI SE ESPECIFICA REVERSE=True SE ORDENA EN ORDEN INVERSO
# lista.sort(reverse=True|False, key=miFunc) = ORDENA LOS ELEMENTOS DE UNA LISTA, SI SE ESPECIFICA REVERSE=True SE ORDENA EN ORDEN INVERSO, SI SE ESPECIFICA LA FUNCION KEY SE ORDENA POR EL VALOR DEVUELTO POR LA FUNCION

#find
txt = "Hola, bienvenido a mi mundo"
x = txt.find("e")
print(x)

#strip
z = "    cadena de prueba   "
print(z, len(z))
z = z.strip()
print(z, len(z))

# replace
cadenaSinGuion = "Hola Mundo Nuevo"
cadenaConGuion = cadenaSinGuion.replace(" ", "-", 1)
print(cadenaConGuion)

# join = unir los elementos de una lista o tupla en una cadena, separados por el separador especificado
miTupla = ("Juan", "Pedro", "Vicky")
x = "#".join(miTupla)
print(x)

# Ordenamiento con key
frutas = ['manzana', 'mango', 'kiwi', 'granadilla']
# Ordena la lista por la longitud de los strings
frutasOrdenadas = sorted(frutas, key=len)
print('Lista ordenada:', frutasOrdenadas)


#! POSICIONAR
variable = 3.141592653589793
print(f"Usando una variable numérica = {variable}")
print(f"|{variable:25}|") # Los números se alinean por defecto al lado derecho
print(f"|{variable:<25}|") # Esto alinea a la izquierda
print(f"|{variable:^25}|")

#! FORMATO DE NUMEROS
variable = 100000
print(f"Esto imprime sin formatear {variable}")
print(f"Esto imprime con formato {variable:,d}")   # d = entero.
print(f"Esto imprime con espaciado y formato {variable:10,d}\n")
variable = 1200356.8796
print(f"Con dos decimales: {variable:.2f}") # f=flotante, .2=dos decimales
print(f"Con cuatro decimales: {variable:.4f}") # f=flotante, .4=cuatro decimales
print(f"Con dos decimales y coma: {variable:,.2f}") # ,=formato con miles, millones

# 
print(f"Número{' '*3}Cuadrado{' '*4}Cubo")
for x in range(1, 11):
    print(f'{x:3d}{" "*7}{x**2:4d}{" "*6}{x**3:5,d}')
    
print(f"Número{' '*3}Cuadrado{' '*5}Cubo")
for x in range(1, 11):
    x = float(x)
print(f'{x:5.2f}{" "*4}{x**2:6.2f}{" "*3}{x**3:8,.2f}')