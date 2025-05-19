from random import randint

lista_correos = []

def es_minuscula(contra):
    minuscula = "abcdefghijklmnopqrstuvwxzy"
    es = False
    for caracter in contra:
        if caracter in minuscula:
            es = True
    return es

def es_mayuscula(contra):
    mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    es = False
    for caracter in contra:
        if caracter in mayuscula:
            es = True
    return es           

def guardar_correo(correo, usuario, direccion, contra, pin):
    guardar = {
        "correo": correo,
        "usuario" : usuario,
        "direccion" : direccion,
        "contra" : contra,
        "pin" : pin
    }
    lista_correos.append(guardar)

def registrar():
    print ("REGISTRAR CORREO")
    correo = input("Ingresar correo: ")
    if "@" in correo:
        usuario, dominio = correo.split("@")
        dominio = "@" + dominio
        if "." in dominio:
            print(dominio)
            contra = input("Contraseña: ")
            if len(contra) <= 8 and es_mayuscula(contra) == True and es_minuscula(contra) == True:
                if "@" in contra or "_" in contra or "$" in contra:
                    pin = randint(100,999)
                    guardar_correo(correo, usuario, dominio, contra, pin)
                    print("CORREO GUARDADO")
                    print(lista_correos)
                else:
                    print("DEBE CONTENER @ _ o $")
            else:
                print("Error contraseña")
        else: 
            print("Error . correo")
    else:
        print("Error @ correo")

def eliminar():
    print ("ELIMINAR CORREO")
    for i, correos in enumerate(lista_correos,start=1):
        print(f"{i}-> Correo {correos["correo"]}, PIN {correos["pin"]}")
    correo = input("Ingresar correo: ")
    encontrado = False  
    for correos in lista_correos:
        if correo == correos[0]:
            lista_correos.remove(correos)
            encontrado = True
    if encontrado == False:
        print("CORREO NO ENCONTRADO")
        
def listado():
    print ("LISTADO DE CORREOS")
    print (f"N°     \tCORREO              \t\tCONTRASEÑA")
    for i, correos in enumerate(lista_correos,start=1):
        print(f"{i}.\t{correos["correo"]}\t\t\t{correos["contra"]}")       

def menu():
    print("BIENVENIDO AL MENU")
    print("1. Registrar correo")
    print("2. Eliminar correo")
    print("3. Listar correos")
    print("4. SALIR")

def main():
    try:
        while True:
            menu()
            opcion = int(input("OPCION: "))
            if opcion == 4:
                break
            elif opcion == 1:
                print("==="*30)
                registrar()
            elif opcion == 2:
                print("==="*30)
                eliminar()
            elif opcion == 3:
                print("==="*30)
                listado()
            else:
                print("ERROR DE OPCION")
    except ValueError:
        print("ERROR")
main()    