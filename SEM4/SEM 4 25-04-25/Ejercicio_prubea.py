

diccionario = {}
cadena = input("Ingrese la cadena de caracteres: ")
for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1

for caracter, cantidad in diccionario.items():
    print(f"El carácter '{caracter}' aparece {cantidad} veces.")

