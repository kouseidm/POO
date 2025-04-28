def menu():
    print("MENU PRINCIPAL")
    print("-"*10)
    print("[1] Pulgadas")
    print("[2] Yardas")
    print("[3] Millas")
    print("[4] Milímetros")
    print("[5] Centímetros")
    print("[6] Metros")
    print("[7] Resumen")
    print("[8] Salir")

def main():
    lista = []
    lista1 = []
    conversiones ={
        1:12,
        2:0.33,
        3:0.0002,
        4:304.8,
        5:30.48,
        6:0.3048,
    }
    unidades = {
    1: "Pulgadas",
    2: "Yaradas",
    3: "Millas",
    4: "Milimetros",
    5: "Centimetros",
    6: "Metros"
    }   
    while True:
        while True:
            menu()
            try:
                opcion = int(input("ingrese una opcion : "))
                if 1<= opcion <=8:
                    break
                else:
                    print("opcion fuera de rango")
            except ValueError:
                print("Error en los datos de ingreso...")

                    
        if opcion == 8:
            break
        if opcion == 7:
            print("N°      pies       convertido a     convertido ")
            for i, (x,y,z) in enumerate(lista,1):
                print(f"{i:}  {x:8}  {y:>15}  {z:14}")
                
        while True:
            try:
                pies = int(input("Ingrese la cantidad de pies a convertir: "))
                if pies > 0:
                    break
                else:
                    print("El dato debe de ser mayor a 0 ")
            except ValueError :
                print("Error en los datos de ingreso...")
                
        if opcion in conversiones:
            valor = conversiones[opcion]
        if opcion in unidades:
            unidad = unidades[opcion]
        conversion = valor * pies
        lista.append((pies,unidad,conversion))
                    
main()