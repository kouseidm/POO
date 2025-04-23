
def triangulos (num):
    for i in range(1,num+1):
        for j in range(i):
            print (j+1, end= " ")
        print ()
    
def main():
    try:
        num = int (input("Ingresar un numero: "))
        if num > 0:
            triangulos(num)
        elif num < 0:
            print("Ingresar un valor positivo")
        
    except ValueError:
        print("Ingresar un valor real")
main()        
