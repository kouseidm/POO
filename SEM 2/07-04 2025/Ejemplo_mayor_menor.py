try:
    while True:
        a=int(input("Ingresa el 1er valor: "))
        b=int(input("Ingresa el 2d valor: "))
        c=int(input("Ingresa el 3er valor: "))
        
        if a!=b and b!=c and a!=c:
            break
    mayor = (a>b and a > c)*a + (b>a and b>c)*b + (c>a and c>b)*c #si (a>b and a > c) es falso tomaria el valor de 0. Para que asi se elimine
    menor = (a<b and a < c)*a + (b<a and b<c)*b + (c<a and c<b)*c 
# (a<b and a < c) una afirmacion si es falsa toma el 0 si es verdadero el 1.
    print ("el mayor es:", mayor)
    print ("el menor es:", menor)
    
except ValueError:
    print ("Error, el valor debe sel un numero entero.")