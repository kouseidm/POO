
def Numero_Capicua(numero):
    num_str = str(numero)
    if num_str == num_str[::-1]:
        print("El número", numero, "es capicúa.")
    else:
        inverso = int(num_str[::-1])
        suma = numero + inverso
        print("El numero no es capicua. La suma del numero y su inversa es:", suma)

def main():
    while True:
        try:
            numero = int(input("Ingrese un numero de 3, 4 o 5 cifras: "))
            if 100 <= numero <= 99999:
                break
            else:
                print("El número debe tener entre 3 y 5 cifras. Intente nuevamente.")
        except ValueError:
            print("El valor debe ser entero positivo")

    Numero_Capicua(numero)

main()