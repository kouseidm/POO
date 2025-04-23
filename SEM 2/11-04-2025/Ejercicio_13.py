def Cuota_variable (esc,cur):
    match esc:
        case 'A': 
            if 1 < cur <= 5:
                monto = 400
            if 5 < cur <= 8:
                monto = 600
            if 8 < cur:
                monto = 900
        case 'B': 
            if 1 < cur <= 3:
                monto = 350
            if 3 < cur <= 7:
                monto = 500
            if 7 < cur:
                monto = 700
        case 'C': 
            if 1 < cur <= 3:
                monto = 320
            if 3 < cur <= 7:
                monto = 480
            if 7 < cur:
                monto = 685
        case 'D': 
            if 1 < cur <= 4:
                monto = 310
            if 4 < cur <= 8:
                monto = 475
            if 8 < cur:
                monto = 680
    return monto

def main():
    while True:
        try:
            
            esc = str(input("Ingrese la escada de pago (A,B,C,D): "))
            if "A" <=esc.upper() <= "D":
                cur = int (input("Ingrese el numero de cursos: "))
                if cur < 0:
                    print ("El valor debe ser un numero entero positivo.")
            else:
                print("El valor ingresado debe ser una letra en mayuscula (A,B,C,D)")

            
            Cuota_variable(esc,cur)
            
            cuota_fija = 350.0

            Importe = cuota_fija + Cuota_variable(esc,cur)

            print ("El importe final sera: ", Importe)
        except ValueError:
            print ("Valores incorrectos.")
main()  