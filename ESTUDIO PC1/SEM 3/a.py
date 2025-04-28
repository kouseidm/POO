while True:
    try:
        n = int(input("Ingresar valor de n: "))
        if n > 0 and n < 11:
            break
        else:
            print("El valor debe ser entre 1 y 10")
    except ValueError:
        print("Valor incorrecto.")
        
for i in range(1,n+1):
    print("  "*(n-i), end="")
    for j in range(1,i*2):
        print(j , end=" ")
    print()
for i in range(n-1,0,-1):
    print("  "*(n-i), end="")
    for j in range(1,i*2):
        print(j , end=" ")
    print()