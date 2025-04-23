def numero_mayor (a,b,c):
    mayor = 0
    if a>b and a>c:
        mayor = a
    elif b>a and b>c:
        mayor = b
    else:
        mayor = c
    return mayor

def numero_menor (a,b,c):
    menor = 0
    if a < b and a < c:
        menor = a
    elif b < a and b < c:
        menor = b
    else:
        menor = c

    return menor

def numero_medio (a,b,c):
    mayor = numero_mayor(a,b,c)
    menor = numero_menor(a,b,c)

    medio = a + b + c - mayor - menor

    print ("Orden descendente: ", mayor , medio , menor)




def main():
    while True:
        try:
            a = int(input("Ingresar el primer numero entero positivo"))
            b = int(input("Ingresar el segundo numero entero positivo"))
            c = int(input("Ingresar el tercer numero entero positivo"))
            if a >= 0 and b>=0 and c >=0:
                break
            else :
                    print ("Todos los valores deben ser enteros positivos")
        except ValueError:
            print ("Todos los valores deben ser enteros positivos")
    numero_menor(a,b,c)
    numero_mayor(a,b,c)
    numero_medio(a,b,c)

main()