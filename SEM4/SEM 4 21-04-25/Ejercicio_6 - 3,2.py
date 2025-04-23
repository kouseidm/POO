def menu ():
    print ("Ingrese a que unidad desea convertir")
    print ("[1] Pulgadas")
    print ("[2] Yardas")
    print ("[3] Millas")
    print ("[4] Milímetros")
    print ("[5] Centímetros")
    print ("[6] Metros")
    print ("[7] Resumen")
    print ("[8] Salir")

    
    
    
            
        
def main ():
    lista = []
    menu()
    while True:
        try:
            opcion = int(input("Ingrese a que unidad desea convertir: "))
            if opcion == 7:
                print ("Conversión de medidas de pies a")
                print ("Nro   Pies   Convertir a      Convertido")
                print ("-----------------------------------------")
                for i,(x,y,z) in enumerate(lista,start=1):
                    print (f"{i:<3} {x:>6} {y:>12} {z:>15}" )
            elif opcion == 8:
                break
            u = float(input("Ingrese la unidad: "))
            if opcion > 0 and opcion < 8:
                match opcion:
                    case 1: 
                        conver = "PULGADAS"
                        resul = u * 12
                        print(f"{u} a PULGADAS es igual a {round (resul,3) }")
                    case 2:
                        conver = "YARDAS"
                        resul = u * 0.33
                        print(f"{u} a YARDAS es igual a {round (resul,3)}")
                    case 3: 
                        conver = "MILLAS"
                        resul = u * 0.0002
                        print(f"{u} a MILLAS es igual a {round (resul,3)}")
                    case 4: 
                        conver = "MILIMETROS"
                        resul = u * 304.8
                        print(f"{u} a MILIMETROS es igual a {round (resul,3)}")
                    case 5: 
                        conver = "CENTIMETROS"
                        resul = u * 30.48
                        print(f"{u} a CENTIMETROS es igual a {round (resul,3)}")
                    case 6: 
                        conver = "METROS"
                        resul = u * 0.3048
                        print(f"{u} a METROS es igual a {round (resul,3)}")
                lista.append ((u, conver, round(resul,3)))
            else:
                print ("El valor debe ser un numero entre 1 y 8.")
        except ValueError: 
            print ("El valor debe ser un numero real")
    
main()