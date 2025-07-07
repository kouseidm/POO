
# -*- coding: utf-8 -*-
import pandas as pd
import ast
import matplotlib.pyplot as plt
from datetime import *
from tabulate import tabulate

# -----------------MOZOS DATA ----------------------#
archivo_mozos = "Mozos.xlsx"
data_mozos = pd.read_excel(archivo_mozos)
#-------------------MEZAS DATA ---------------------#
archivo_mesas = "Mesas.xlsx"
data_mesas = pd.read_excel(archivo_mesas)
#---------------------------------------------------#
# -----------------PEDIDOS DATA ----------------------#
archivo_pedidos = "Pedidos.xlsx"
data_pedidos = pd.read_excel(archivo_pedidos)
# -----------------CARTA DATA ----------------------#
archivo_carta= "Carta.xlsx"
data_carta = pd.read_excel(archivo_carta)

class Restaurante:
    def __init__(self, Mozos, Mesas):
        self.__mozos = Mozos
        self.__Mesas = Mesas
    
    @property
    def mosos (self):
        return self.__mozos
    
    @property
    def mesas (self):
        return self.__Mesas
    def guardar_mesas (self,mesa):
        archivo_mesas = "Mesas.xlsx"
        data_mesas = pd.read_excel(archivo_mesas)
        nueva_mesa = {
            "numero_mesa": mesa.numeroMesa,
            "zona_mesa": mesa.zonaMesa,
            "capacidad_mesa": mesa.capacidad,
            "estado_mesa": mesa.estado
        }
        
        data_mesas = pd.concat([data_mesas, pd.DataFrame([nueva_mesa])], ignore_index=True)
        data_mesas.to_excel("Mesas.xlsx", index= False)
    
      #|id_mozo | nombre|telefono | estado |mesas_reservadas
    def guardar_mozos (self,mozo):
        archivo_mozos = "Mozos.xlsx"
        data_mozos = pd.read_excel(archivo_mozos)
        nuevo_mozo = {
            "id_mozo": mozo.idMozo,
            "nombre": mozo.nombre,
            "telefono": mozo.telefono,
            "estado": mozo.estado,
            "mesas_reservadas": []
        }
        
        data_mozos = pd.concat([data_mozos,pd.DataFrame([nuevo_mozo])], ignore_index= True)
        data_mozos.to_excel("Mozos.xlsx", index=False)
    
    def guardar_Pedidos (self,pedidos):
        archivo_pedidos = "Pedidos.xlsx"
        data_pedidos = pd.read_excel(archivo_pedidos)
        nuevo_pedidos = {
            "num_mesa": pedidos.num_mesa,
            "num_mozo": pedidos.num_mozo,
            "pedido": pedidos.pedido,
            "fecha": pedidos.fecha,
            "fecha_en": pedidos.fecha_en,
            "entregado": pedidos.entregado,
            "pagos": pedidos.pagos
        }
        
        data_pedidos = pd.concat([data_pedidos, pd.DataFrame([nuevo_pedidos])], ignore_index=True)
        data_pedidos.to_excel("Pedidos.xlsx", index=False)
    
    # ?------------------------------------------------------------------------------
    def r_registros(self):
        # Mostrar el reporte de mesas registradas
        print("-" * 80)
        print("MESAS REGISTRADAS".center(80))
        print("Terraza: ", len(data_mesas[data_mesas["zona_mesa"] == "Terraza"] ["numero_mesa"].tolist()), "mesas")
        print("Sala   : ", len(data_mesas[data_mesas["zona_mesa"] == "Sala"]["numero_mesa"].tolist()), "mesas")
        print("TOTAL DE REGISTROS PERMITIDOS POR EL RESTAURANTE: 50 MESAS")
        print("20 MESAS EN TERRAZA Y 30 MESAS EN SALA".center(56))
        print("-" * 80)
        while True:
            opcion = input("Desea ver el grafico (si/no): ").lower()
            if opcion in ["si", "no"]:
                break
            else:
                print("Respuesta incorrecta")
        
        if opcion == "si":
            terraza = len(data_mesas[data_mesas["zona_mesa"] == "Terraza"] ["numero_mesa"].tolist())
            sala  =  len(data_mesas[data_mesas["zona_mesa"] == "Sala"]["numero_mesa"].tolist())
            etiquetas = ["Sala", "Terraza"]
            valores = [sala, terraza]
            colores = ["green", "orange"]
            plt.bar(etiquetas, valores,color = colores)
            plt.title("Reporte de mesas por zona")
            plt.ylabel("Cantidad mesas")
            plt.xlabel("Zona")
            for i, v in enumerate(valores):
                plt.text(i,v,str(v), ha = "center", va = "bottom")
            plt.show()
            
        else:
            print("saliendo ....... ")
    
        
    # ?------------------------------------------------------------------------------
        
    def existe_mesa (self, numero_mesa):
        if numero_mesa in data_mesas["numero_mesa"].values:
            return True
        else:
            return False

    def existe_mozo (self, num_mozo):
        if num_mozo in data_mozos["id_mozo"].values:
            return True
        else:
            return False        

    def registrar_mesas(self):
        global data_mesas
        # Ingresamos el numero de mesa
        #   | numero_mesa | zona_mesa | capacidad_mesa | estado_mesa  --> Nombres de la tabla de datos
        print("Registro de mesas".center(80, "-"))
        while True:
            try:
                numero_mesa = int(input("Ingrese el numero de mesa a registrar (1 - 50): "))
                if 1<= numero_mesa <= 50:
                    if numero_mesa in data_mesas["numero_mesa"].values:
                        print("Error, la mesa ya  esta registrada")
                        return
                    else:
                        break
                else:
                    print("Error, el numero de mesa esta fuera de rango (50 mesas maximo)")
            except ValueError:
                print("Error en los datos de ingreso")
        while True:
            zona_mesa = input("Ingrese la zona de disponibilidad de la mesa (Sala/Terraza): ").title()
            if zona_mesa in ["Sala", "Terraza"]:
                break
            else:
                print("Error, la zona de registro no es correcta")
                
                
                
        # ?------------------------------------------------------------------------------
        # Validamos la zona de la mesa
        if zona_mesa == "Sala":
            if len(data_mesas[data_mesas["zona_mesa"] == "Sala"]) >= 30:
                print("Error, ya se han registrado 30 mesas en la zona Sala")
                return
        if zona_mesa == "Terraza":
            if len(data_mesas[data_mesas["zona_mesa"] == "Terraza"]) >= 20:
                print("Error, ya se han registrado 20 mesas en la zona Terraza")
                return
        # ?------------------------------------------------------------------------------
        
        while True:
            try:
                capacidad_mesa = int(input("Ingrese la capacidad de la mesa ( 1 - 4): "))
                if 1<= capacidad_mesa <= 4:
                    break
                else:
                    print("Error, la capacidad de la mesa no es correcta")
            except ValueError:
                print("Error en los datos de ingreso")
        
        while True:
            estado_mesa = input("Ingrese el estado de la mesa (Libre/Reservada): ").title()
            if estado_mesa in ["Libre", "Reservada"]:
                break 
            else:
                print("Error, el estado de mesa no es correcto")
        mesa = Mesas(numero_mesa, zona_mesa,capacidad_mesa, estado_mesa)
        self.guardar_mesas(mesa)
        data_mesas = pd.read_excel("Mesas.xlsx")
        print("-" * 80)
        print("Mesa registrada correctamente".center(80))
        print("-" * 80)
    
    # ?------------------------------------------------------------------------------
    def reporte_mozos(self):
        # Mostrar el reporte de mozos registrados
        print("-" * 80)
        print("MOZOS REGISTRADOS".center(80))
        print("Total de mozos registrados: ", len(data_mozos))
        print("Mozos activos  : ", len(data_mozos[data_mozos["estado"] == "Activo"]))
        print("Mozos inactivos: ", len(data_mozos[data_mozos["estado"] == "Inactivo"]))
        print("-" * 80)
        
        while True:
            opcion = input("Desea ver el grafico  (si/no): ").lower()
            if opcion in ["si", "no"]:
                break 
            else:
                print("Respuesta incorrecta")
        
        if opcion == "si":
            activos  = len(data_mozos[data_mozos["estado"] == "Activo"])
            inactivos  = len(data_mozos[data_mozos["estado"] == "Inactivo"])
            
            etiquetas = ["Activos", "Inactivos"]
            valores = [activos, inactivos]
            colores = ["skyblue", "green"]
            plt.bar(etiquetas, valores, color = colores)
            plt.title("Reporte de mozos")
            plt.ylabel("Cantidad")
            plt.xlabel("Estado")
            for i, v in enumerate(valores):
                plt.text(i,v, str(v), ha = "center", va= "bottom")
            plt.show()
        else:
            print("saliendo ...... ")
            
            
    # ?------------------------------------------------------------------------------
    
    #|id_mozo | nombre|telefono | estado |mesas_reservadas --> Nombre de datos del mozo
    def registrar_mozos (self):
        global data_mozos
        print("-" * 80)
        print("Registro de mozos".center(80, "-"))
        print("-" * 80)
        while True:
            existe_mzo = False
            id_mozo = input("Ingrese el id del mozo ( 4 digitos): ")
            if len(id_mozo) == 4 and id_mozo.isdigit():
                if int(id_mozo) in data_mozos["id_mozo"].values:
                    print("Error, el mozo ya esta registrado")
                    return
                else:
                    break
            else:
                print("El id debe ser de 4 digitos numericos")
        while True:
            nombre_mozo = input("Ingrese el nombre y apellido del mozo: ")
            contiene_numero = False
            for caracter in nombre_mozo:
                if caracter.isdigit():
                    contiene_numero = True
                    print("El nombre no debe tener numeros")
                    break
            if not contiene_numero:
                break
        
        while True:
            try:
                telefono_mozo = input("Ingrese el telefono del mozo (9 digitos): ")
                if len(telefono_mozo) == 9 and telefono_mozo.isdigit():
                    if int(telefono_mozo) in data_mozos["telefono"].values:
                        print("Error el telefono ya esta registrado")
                    
                    else: 
                        break
                else:
                    print("Error el telefono no es correcto")
            except ValueError:
                print("Error datos de ingreso incorrectos")
        
        while True:
            estado_mozo = input("Ingrese el estado del mozo (Activo/Inactivo) sin espacios: ").title()
            if estado_mozo in ["Activo", "Inactivo"]:
                break
            else:
                print("Error, el estado del mozo no es correcto")
        mozo = Mozos(id_mozo,nombre_mozo, telefono_mozo,estado_mozo)    
        self.guardar_mozos(mozo)
        data_mozos = pd.read_excel("Mozos.xlsx")
        print("-" * 80)
        print("Mozo registrado correctamente".center(80))
        print("-" * 80)


    def reportes_pedidos(self):
        data_pedidos = pd.read_excel(archivo_pedidos)
        print("-" * 80)
        print("PEDIDOS REGISTRADOS".center(80))
        print("Total de PEDIDOS registrados: ", len(data_pedidos))
        print("Pedidos entregados: ", len(data_pedidos[data_pedidos["entregado"] == "si"]))
        print("Pedidos no entregados: ", len(data_pedidos[data_pedidos["entregado"] == "no"]))
        print("-" * 80)
        
        while True:
            opcion = input("Desea ver el grafico: ").lower()
            if opcion in ["si", "no"]:
                break 
            else:
                print("Error en los datos de ingreso")
        if opcion == "si":
            pedidos_e = len(data_pedidos[data_pedidos["entregado"] == "si"])
            pedidos_no_e = len(data_pedidos[data_pedidos["entregado"] == "no"])
            
            titulos = ['Entregado', 'No entregados']
            valores = [pedidos_e, pedidos_no_e]
            leyendas = ['Entregado', 'No entregado']
            
            plt.pie(valores, labels=titulos, autopct='%1.1f%%')
            plt.legend(leyendas)
            plt.title('PEDIDOS REGISTRADOS')
            plt.show()
        else:
            print("saliendo ..... ")
            
        
    # num_mesa | num_mozo | pedido | fecha
    def r_pedidos(self):
        print("-" * 80)
        print("Tomar Pedido".center(80))
        print("-" * 80)
        
        archivo_pedidos = "Pedidos.xlsx"
        data_pedidos = pd.read_excel(archivo_pedidos)
        
        while True:
            num_mesa = int(input("Ingresar el numero de mesa: "))
            if self.existe_mesa(num_mesa) == False:
                print("la mesa debe estar registrada") 

            else:
                pedidos_en_mesa = data_pedidos[
                    (data_pedidos["num_mesa"] == num_mesa) & (data_pedidos["entregado"] == "no")
                ]
                if not pedidos_en_mesa.empty:
                    print("Ya hay un pedido registrado en esa mesa.")
                    continue                        
                
                estado_mesa = data_mesas.loc[data_mesas["numero_mesa"] == num_mesa, "estado_mesa"].values[0]
                if estado_mesa == "Libre":
                    print("La mesa esta libre.")
                    break
                else:
                    print("La mesa ya esta reservada.")
                #agregar 1 cliente a la mesa 
                 
        while True:
            num_mozo = int(input("Ingresar el numero del mozo: "))
            if self.existe_mozo(num_mozo) == False:
                print("El mozo no esta registrado") 
            else:
                estado_mozo = data_mozos.loc[data_mozos["id_mozo"] == num_mozo, "estado"].values[0]
                if estado_mozo == "Activo":
                    print("El mozo está activo.")
                    break  
                else:
                    print("El mozo está inactivo, elija otro mozo.")
        fecha = 0   
        fecha_en = 0
        entregado = "no"
        lista_pedido = []
        while True:
            opcion = input("Desea agregar un pedido?: ").upper()
            if opcion == "SI":
                fecha = datetime.now().strftime("%Y/%m/%d %H:%M")
                self.mostrar_carta()
                pedido = int(input("Ingrese el id del pedido que desea: "))
                
                
                # ?------------------------------------------------------------------------------
                # Actualizar el estado de la mesa a "Reservada"
                data_mesas.loc[data_mesas["numero_mesa"] == num_mesa, "estado_mesa"] = "Reservada"
                data_mesas.to_excel("Mesas.xlsx", index=False)
                # ?------------------------------------------------------------------------------
                
                
                id_pedido = data_carta.loc[data_carta["idCarta"] == pedido]
                if not id_pedido.empty: 
                    lista_pedido.append(id_pedido.iloc[0].to_dict())
                    print("Pedido agregado:", id_pedido.iloc[0].to_dict())
                
                
                # ?------------------------------------------------------------------------------
                    # Agregar la mesa con pedidos registrados a mesas asignadas
                    mozo_index = data_mozos[data_mozos["id_mozo"] == num_mozo].index[0]
                    mozo = data_mozos.loc[mozo_index]
                    
                    # Cargar mesas reservadas
                    m_reservadas = mozo["mesas_reservadas"]
                    if isinstance(m_reservadas, str):
                        m_reservadas = eval(m_reservadas)
                    else:
                        m_reservadas = []

                    # Actualizar los datos del mozo 
                    if num_mesa not in m_reservadas:
                        m_reservadas.append(num_mesa)
                        data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
                        data_mozos.to_excel("Mozos.xlsx", index = False)
                    
                    # Cambiar el estado del mozo a "Inactivo" si tiene 4 mesas asignadas
                    if len(m_reservadas) >= 4:
                        data_mozos.at[mozo_index, "estado"] = "Inactivo"
                        data_mozos.to_excel("Mozos.xlsx", index=False)
                        print(f"El mozo {mozo['nombre']} ahora está inactivo.")
                # ?------------------------------------------------------------------------------
            
            
                else:
                    print("El id del pedido no existe en la carta.")
                    
            elif opcion == "NO":
                print("Estaremos en espera de su respuesta")
                break
            else:
                print("Debe ser si o no")

            print("REGISTRO DE PEDIDO")
        
        pagos = 0
        pedido = Pedidos(num_mesa, num_mozo, lista_pedido, fecha, fecha_en, entregado, pagos)    
        self.guardar_Pedidos(pedido)
        print("-" * 80)
        print("Pedido registrado correctamente".center(80))
        print("-" * 80)

    def finalizar_pedido(self):
        while True:
            archivo_pedidos = "Pedidos.xlsx"
            data_pedidos = pd.read_excel(archivo_pedidos) 
            
            while True:  
                try:
                    num_mesa = int(input("Ingresar el numero de mesa: "))
                    if num_mesa > 0:
                        break 
                    else:
                        print("Numero de mesa incorrecto")
                except ValueError:
                    print("Error en el ingreso de datos")
                    
            pedidos_mesa = data_pedidos[data_pedidos["num_mesa"]==num_mesa]
            if not pedidos_mesa.empty:
                ultimo_pedido = pedidos_mesa.iloc[-1]# seleccionar el pedido correcto
                if ultimo_pedido['pedido'] == "[]":
                    print("No hay pedidos para finalizar")
                    break
            else:
                print("No hay pedidos registrados en esta mesa")
                return 
            
            if str(ultimo_pedido["entregado"]) == "si":
                print("-"*30)
                print("Este pedido ya fue entregado.")
                break
            
            if self.existe_mesa(num_mesa) == False:
                print("la mesa debe estar registrada") 
            else:
                while True:
                    productos = ast.literal_eval(ultimo_pedido["pedido"]) 
                    cantidad = len(productos)
                    fecha_pedido = pedidos_mesa.iloc[-1]["fecha"]
                    fecha_format = datetime.strptime(fecha_pedido, "%Y/%m/%d %H:%M")
                    print(f"La mesa {num_mesa} tiene {cantidad} de pedidos registrado a las {fecha_format.hour}:{fecha_format.minute:02d} ")
                    print("-"*30)
                    opcion = input("Recibio correctamente su pedido? ").upper()
                    if opcion in ['SI', 'NO']:
                        if opcion == "SI":
                            
                                while True:
                                    try:
                                        print("-"*30)
                                        print("Registre la hora en la que se recibio el pedido (formato 24h)")
                                        hora_entrega = int(input("Hora: "))
                                        minuto_entrega = int(input("Minutos: "))
                                        
                                        if 0 <= hora_entrega < 24 and 0 <= minuto_entrega < 60:
                                            entrega_aux  = fecha_format.replace(hour=hora_entrega, minute=minuto_entrega)
                                            if entrega_aux  <= fecha_format:
                                                entrega_aux  += timedelta(days=1)
        
                                            fecha_entrega = entrega_aux.strftime("%Y/%m/%d %H:%M")
                                            indice_pedido = data_pedidos[data_pedidos["num_mesa"] == num_mesa].index[-1]
                                            data_pedidos.at[indice_pedido, "fecha_en"] = fecha_entrega
                                            data_pedidos.at[indice_pedido, "entregado"] = "si"
                                            data_pedidos.to_excel(archivo_pedidos, index=False)
                                            print("-"*30)
                                            print("Fecha de entrega registrada correctamente.")
                                            break
                                        else:
                                            print("El tiempo a la hora de entrega es incorrecta")
                                    except ValueError:
                                        print("Introducir numeros")
                                #?------------------------------------------------------------------------------
                                # Actualizar el estado de la mesa a "Libre"
                                data_mesas.loc[data_mesas["numero_mesa"] == num_mesa, "estado_mesa"] = "Libre"
                                
                                # eliminar la mesa de las mesas reservadas del mozo
                                mozo_id = ultimo_pedido["num_mozo"]
                                if mozo_id in data_mozos["id_mozo"].values:
                                    mozo_index = data_mozos[data_mozos["id_mozo"] == mozo_id].index[0]
                                    m_reservadas = data_mozos.at[mozo_index, "mesas_reservadas"]
                                    if isinstance(m_reservadas, str):
                                        m_reservadas = ast.literal_eval(m_reservadas)
                                    else:
                                        m_reservadas = []
                                    
                                    if num_mesa in m_reservadas:
                                        m_reservadas.remove(num_mesa)
                                        data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
                                        if len(m_reservadas) < 4:
                                            data_mozos.at[mozo_index, "estado"] = "Activo"
                                        data_mozos.to_excel("Mozos.xlsx", index=False)
                                else:
                                    print("El mozo no está registrado")
                                
                                data_mesas.to_excel("Mesas.xlsx", index=False)
                                #?------------------------------------------------------------------------------
                                
                                print("-"*30)
                                print("Muchas gracias por la espera, disfrute su comida.")
                                break
                        else:
                            print("Lamestamos el servicio, posteriormente se aplicara un descuento")
                        break
                    else:
                        print("Opcion incorrecta [si o no]")
                break
            
    def modificar_pedido(self):

            archivo_pedidos = "Pedidos.xlsx"
            data_pedidos = pd.read_excel(archivo_pedidos)
            while True:
                try:
                    nMesa=int(input("Digite el numero de mesa: ")) 
                    if nMesa > 0:
                        break 
                except ValueError:
                    print("El numero de mesa es incorrecta")
                    
            fila_mesa = data_pedidos[data_pedidos["num_mesa"] == nMesa]
            
            if self.existe_mesa(nMesa)==False:
                print("Error, la mesa no esta registrada.")
                return
            
            #validar que el pedido no este pagado
            ultimo_pedido = fila_mesa.iloc[-1]
            if ultimo_pedido["pagos"] != 0:
                print("El pedido ya ha sido pagado")
                return

            #validar que el pedido no este entregado
            if ultimo_pedido["entregado"] == "si":
                print("El pedido ya ha sido entregado")
                return 



            
            print(" ")
            print(f"----PEDIDOS REGISTRADOS EN LA MESA {nMesa}----".center(60))
            print(" ")
            
            if fila_mesa.empty:
                print("No hay pedidos registrados en la mesa")
                return
            ultimo_pedido = fila_mesa.iloc[-1]
            pedidos = ast.literal_eval(ultimo_pedido["pedido"]) if ultimo_pedido["pedido"] else []
            if not pedidos:
                print(f"La mesa {nMesa} no tiene pedidos registrados. ")
            else:
                nombre_precio = [f"{i['nombre']}(S/{i['precio']})" for i in pedidos]
                x = ", ".join(nombre_precio)
                print(tabulate([[ultimo_pedido["num_mesa"], x]], headers=["num_mesa", "pedido"], tablefmt="grid"))
                    
                
            while True:
                print(" ")
                print("1. Agregar pedido")
                print("2. Anular pedido" )
                print("3. Salir         ")
                while True:    
                    try:
                        n=int(input("\nIndique la opcion que desea:  "))
                        if 1<= n <= 4:
                            break
                        else:
                            print("Error, ingrese una opcion válida. ")
                    except ValueError:
                        print("Error, digite un numero. ")
                        
                if n==1:
                    self.mostrar_carta()
                    pedido = int(input("Ingrese el id del pedido que desea: "))
                    id_pedido = data_carta.loc[data_carta["idCarta"] == pedido]
                    if not id_pedido.empty: 
                        
                        fecha = datetime.now().strftime("%Y/%m/%d %H:%M")
                        
                        pedidos.append(id_pedido.iloc[0].to_dict())
                        print("Pedido agregado:", id_pedido.iloc[0].to_dict())
                        idx = fila_mesa.index[-1]
                        data_pedidos.at[idx, "pedido"] = str(pedidos)
                        data_pedidos.at[idx, "fecha"] = fecha
                        data_pedidos.to_excel("Pedidos.xlsx", index=False)
                    else:
                        print("Error, el pedido no existe en la carta. ")
                            
                elif n==2:
                    if not pedidos:
                        print("No hay productos para anular.")
                        continue
                    print("Productos actuales:")
                    for idx, prod in enumerate(pedidos):
                        print(f"{idx+1}. {prod['nombre']} (S/{prod['precio']})")
                    try:
                        num = int(input("Ingrese el número del producto a eliminar: "))
                        if 1 <= num <= len(pedidos):
                            
                            fecha = datetime.now().strftime("%Y/%m/%d %H:%M")
                            
                            eliminado = pedidos.pop(num-1)
                            print(f"Producto '{eliminado['nombre']}' eliminado del pedido.")
                            idx_pedido = fila_mesa.index[-1]
                            data_pedidos.at[idx_pedido, "pedido"] = str(pedidos)
                            data_pedidos.at[idx_pedido, "fecha"] = fecha
                            data_pedidos.to_excel("Pedidos.xlsx", index=False)
                        else:
                            print("numero invalido.")
                            
                    except ValueError:
                        print("Error de digito")
                    
                elif n==3:
                    break

    def realizar_pago(self):
        print("-" * 50)
        print("<< CALCULO >>".center(61))
        print("-" * 50)
        print("MESA A REALIZAR EL PAGO ")
        while True: 
            try:  
                n=int(input("--> "))
                if self.existe_mesa(n)==False:
                    print("Error, la mesa no esta registrada.")
                else:
                    archivo_pedidos = "Pedidos.xlsx"
                    data_pedidos = pd.read_excel(archivo_pedidos)
                    mesa=data_pedidos[data_pedidos["num_mesa"]==n]
                    
                    ultimo_pedido = mesa.iloc[-1]
                    if ultimo_pedido["pagos"] != 0:
                        print(f"El último pedido de la mesa {n} ya está pagado.")
                        return 0
                    
                    #----------------------------------------------------------------------
                    hora_registro=mesa.iloc[-1]["fecha"]
                    fecha_format1 = datetime.strptime(hora_registro, "%Y/%m/%d %H:%M")
                    #----------------------------------------------------------------------
                    hora_entrega=mesa.iloc[-1]["fecha_en"]
                    #----------------------------------------------------------------------
                    # convertir todo a min
                    cont_registro= fecha_format1.hour*60 + fecha_format1.minute
                    if hora_entrega=="sin_fecha" or hora_entrega==0:
                        print(f"El pedido de la mesa {n} no ha sido entregado.")
                        return 0
                    else:
                        fecha_format2 = datetime.strptime(hora_entrega, "%Y/%m/%d %H:%M")
                        conv_entrega= fecha_format2.hour*60+fecha_format2.minute
                        limite_entrega= cont_registro+30
                        suma_pagos=0
                        pedidos_jiji=mesa.iloc[-1]["pedido"]
                        pedidos_jojo=ast.literal_eval(pedidos_jiji)
                        if isinstance(pedidos_jojo, list):
                            #suma_pagos=0
                            only_precios=[]
                            
                            for i in pedidos_jojo:
                                precio=i["precio"]
                                #platicos= i["pedidos"]
                                suma_pagos+=precio
                                only_precios.append(f"{i['nombre']} S/{precio}")
                            p=", ".join(only_precios)
                            mesa.loc[:, "pedido"]=p
                                    
                            columnas=["num_mesa", "pedido"]
                            print( " ")
                            print(tabulate(mesa.iloc[[-1]][columnas], headers="keys", tablefmt="plain"))
                            print(" ")
                            print("---------------------------")
                            print(f"Total       PEN --> {suma_pagos}")
                            if conv_entrega>limite_entrega:
                                print("\n¡¡SE APLICARÁ DESCUENTO 10% POR EL TIEMPO DE ESPERA!!")
                                print("_____________________________________________________")
                            #suma_pagos=0
                            #try:
                            
                            descuento_wa= suma_pagos*0.1
                            suma_pagos=suma_pagos-descuento_wa
                            print(f"Total con 10% de descuento: S/{descuento_wa:.2f}")
                            print(f"El nuevo pago Total   PEN --> {suma_pagos} ")
                            propina=str(input("Desea agregar propina del 10% (SI/NO): ")).lower()
                            if propina=="si":
                                suma_pagos+=suma_pagos*0.10
                                print("-- PAGO --")
                                print(" ")
                                print(f"Total       PEN --> {suma_pagos}")           
                            elif propina=="no":
                                print("Correcto. Se omitio la propina.")    
                            idx=data_pedidos[data_pedidos["num_mesa"]==n].index[-1]
                            data_pedidos.at[idx, "pagos"]=suma_pagos
                            data_pedidos.to_excel(archivo_pedidos,index=False)
                            return suma_pagos     
                        else:
                            print("No hay pedidos válidos para esta mesa.")
            except ValueError:
                print("Error en los datos de ingreso")

    def guardar_carta (self,carta):
        nueva_carta = {
            "idCarta": carta.idCarta,
            "nombre": carta.nombre,
            "tipo": carta.tipo,
            "precio":carta.precio
        }
        nueva_data = pd.concat([data_carta, pd.DataFrame([nueva_carta])], ignore_index=True)
        nueva_data.to_excel("Carta.xlsx", index=False)
    def agregar_carta(self):
        print("=" * 50)
        print("REGISTRAR NUEVA CARTA".center(50))
        print("=" * 50)
        idCarta=input("ingrese la id: ")
        nombre=input("ingrese el nombre: ")
        while True:
            tipo= input("ingrese el tipo (plato,postre,bebida): ")
            if tipo.lower() in ["plato","postre","bebida"]:
                break
            else:
                print("escriba correctamente")
        precio=float(input("ingrese el precio: "))
        carta=Carta(idCarta,nombre,tipo,precio)
        self.guardar_carta(carta)
        
    def modificar_carta(self):
        print("=" * 50)
        df_carta = pd.read_excel("Carta.xlsx")
        self.mostrar_carta()
        while True:
            try:
                idCarta=input("ingrese el id de la carta a editar: ")
            except ValueError:
                print("Error en los datos de ingreso")
                
            if idCarta in df_carta["idCarta"].astype(str).values:
                plato_index = df_carta[df_carta["idCarta"].astype(str) == idCarta].index[0]
                while True:
                    try:
                        nuevo_precio=float(input("ingrese el nuevo precio: "))
                        if nuevo_precio>0:
                            df_carta.at[plato_index, "precio"] = nuevo_precio
                            df_carta.to_excel("Carta.xlsx", index=False)
                            return
                        else:
                            print("el precio debe ser mayor a 0")
                            return
                    except ValueError:
                        print("Error en los datos de ingreso")
            else:
                print("El id ingresado no está en la carta")
    def eliminar_carta(self):
        df_carta = pd.read_excel("Carta.xlsx")
        self.mostrar_carta()
        while True:
            try:
                idEliminar=int(input("Ingrese el id de la carta a eliminar: "))
                if idEliminar > 0:
                    break
            except ValueError:
                print("Error en el ingreso de datos")
                
        if idEliminar not in df_carta["idCarta"].values:
            print("No existe ese ID en la carta")
            return
        df_carta=df_carta[df_carta["idCarta"]!=idEliminar]
        df_carta.to_excel("Carta.xlsx",index=False)
        print("eliminado exitosamente")
        
    def mostrar_carta(self):
        df_carta = pd.read_excel("Carta.xlsx")
        platos_imprimir=[]
        postre_imprimir=[]
        bebida_imprimir=[]
        
        for i in df_carta.index:
            tipo=df_carta["tipo"][i]
            if tipo=="plato":
                platos_imprimir.append((df_carta["idCarta"][i],df_carta["nombre"][i],df_carta["precio"][i]))
            if tipo=="postre":
                postre_imprimir.append((df_carta["idCarta"][i],df_carta["nombre"][i],df_carta["precio"][i]))
            if tipo=="bebida":
                bebida_imprimir.append((df_carta["idCarta"][i],df_carta["nombre"][i],df_carta["precio"][i]))
        print("="*30)
        print("PLATOS".center(30))
        print("="*30)
        print(tabulate(platos_imprimir,headers=["IdCarta","Nombre","Precio"],tablefmt="grid"))
        print("="*30)
        print("POSTRES".center(30))
        print("="*30)
        print(tabulate(postre_imprimir,headers=["IdCarta","Nombre","Precio"],tablefmt="grid"))
        print("="*30)
        print("BEBIDAS".center(30))
        print("="*30)
        print(tabulate(bebida_imprimir,headers=["IdCarta","Nombre","Precio"],tablefmt="grid"))


    def mozo_mas_pedido(self):
        data_pedidos=pd.read_excel("Pedidos.xlsx")
        data_mozos=pd.read_excel("Mozos.xlsx")
        imprimir=[]
        
        for i in data_mozos.index:
            mesas_atendidas=0
            total_pedidos=0
            for j in data_pedidos.index:
                if data_mozos["id_mozo"][i] == data_pedidos["num_mozo"][j]:
                    pedido=ast.literal_eval(data_pedidos["pedido"][j])
                    total_pedidos+=len(pedido)
                    mesas_atendidas+=1
            if total_pedidos>0:
                imprimir.append((data_mozos["id_mozo"][i],data_mozos["nombre"][i],str(data_mozos["telefono"][i]),total_pedidos,mesas_atendidas))
        if not imprimir:
            print("No hay mozos con pedidos registrados")
            return
        imprimir.sort(key=lambda x: x[3],reverse=True)
        mozo_mas_pedido=imprimir[0]
        print(tabulate(imprimir,headers=["ID","Nombre","Telefono","Total pedidos","Mesas atendidas"],tablefmt="grid"))
        print("="*60)
        print("EL MOZO CON MÁS PEDIDOS")
        print("-"*60)
        print(f"Mozo: {mozo_mas_pedido[1]}, con un total de pedidos de: {mozo_mas_pedido[3]}")
        print("="*60)
        while True:
            opc=input("¿Desea ver un gráfico de los 10 mozos con más pedidos?: ").lower()
            print("="*50)
            if opc in ["si","sí","s"]:
                mozos=[]
                pedidos=[]
                
                for i in range(0,10):
                    mozos.append(str(imprimir[i][0]))
                    pedidos.append(imprimir[i][3])
                mozos.reverse()
                pedidos.reverse()
                plt.bar(mozos,pedidos,color="coral")
                plt.title("TOP 10 MOZOS CON MÁS PEDIDOS")
                plt.xlabel("MOZOS(ID)")
                plt.ylabel("PEDIDOS")
                for i, v in enumerate(pedidos):
                    plt.text(i, v , str(v), ha = "center", va = "bottom")
                plt.show()
                break
            elif opc in ["no","n"]:
                break
            
    def prom_tiempo_e(self):
        data_pedidos=pd.read_excel("Pedidos.xlsx")
        p_fecha_entr= data_pedidos[data_pedidos["fecha"] != 0]
        p_fecha_entr= data_pedidos[data_pedidos["fecha_en"] != 0]
        
        p_entregados=0
        tiempo_total=0
        for i in p_fecha_entr.index:

            fecha_pedido= ((p_fecha_entr["fecha"][i])[8:16]).replace(":","")
            dia_pedido=fecha_pedido[0:2]
            hora_pedido=int(fecha_pedido[3:5])
            minuto_pedido=int(fecha_pedido[5:7])


            fecha_en_val = p_fecha_entr["fecha_en"][i]
            if not isinstance(fecha_en_val, str):
                continue 
            fecha_entrega=((p_fecha_entr["fecha_en"][i])[8:16]).replace(":","")
            dia_entrega=fecha_entrega[0:2]
            hora_entrega=fecha_entrega[3:5]
            minuto_entrega=int(fecha_entrega[5:7])
            
            if dia_pedido != dia_entrega:
                if hora_entrega == "00":
                    tiempo_pedido=hora_pedido*60+minuto_pedido
                    tiempo_entrega= (int(hora_entrega)+24)*60+minuto_entrega
                    tiempo_total+= tiempo_entrega-tiempo_pedido
                    p_entregados+=1
                elif hora_entrega == "01":
                    tiempo_pedido=hora_pedido*60+minuto_pedido
                    tiempo_entrega= (int(hora_entrega)+25)*60+minuto_entrega
                    tiempo_total+= tiempo_entrega-tiempo_pedido
                    p_entregados+=1
            else:
                tiempo_pedido=hora_pedido*60+minuto_pedido
                tiempo_entrega= (int(hora_entrega))*60+minuto_entrega
                tiempo_total+= tiempo_entrega-tiempo_pedido
                p_entregados+=1
                
        promedio_espera= tiempo_total/p_entregados
        if p_entregados == 0:
            print("No hay pedidos completos con hora de entrega registrada")
            return
        print("="*50)
        print(f"TIEMPO PROMEDIO DE ESPERA")
        print("-"*50)
        print(f"Promedio de espera: {promedio_espera:.1f} minutos")
        print("="*50 + "\n")
        
        
    def pedidos_tardes(self):
        data_pedidos=pd.read_excel("Pedidos.xlsx")
        p_fecha_entr= data_pedidos[data_pedidos["fecha"] != 0]
        p_fecha_entr= data_pedidos[data_pedidos["fecha_en"] != 0]
        pedidos_tardios=0
        pedidos_a_tiempo=0
        
        for i in p_fecha_entr.index:

            fecha_pedido=((p_fecha_entr["fecha"][i])[8:16]).replace(":","")
            dia_pedido=fecha_pedido[0:2]
            hora_pedido=int(fecha_pedido[3:5])
            minuto_pedido=int(fecha_pedido[5:7])


            fecha_en_val = p_fecha_entr["fecha_en"][i]
            if not isinstance(fecha_en_val, str):
                continue 
            fecha_entrega=((p_fecha_entr["fecha_en"][i])[8:16]).replace(":","")
            dia_entrega=fecha_entrega[0:2]
            hora_entrega=fecha_entrega[3:5]
            minuto_entrega=int(fecha_entrega[5:7])

            if dia_pedido != dia_entrega:
                if hora_entrega == "00":
                    minuto_entrega=minuto_entrega+60
                    if minuto_entrega-minuto_pedido>30:
                        pedidos_tardios+=1
                    else:
                        pedidos_a_tiempo+=1
                else:
                    pedidos_tardios+=1
            else:
                if (int(hora_entrega)*60+minuto_entrega)-(hora_pedido*60+minuto_pedido)>30:
                    pedidos_tardios+=1
                else:
                    pedidos_a_tiempo+=1
        total_pedidos=pedidos_tardios+pedidos_a_tiempo
        print("="*50)
        print("PEDIDOS TARDIOS")
        print("-"*50)
        print(f"De un total de {total_pedidos} pedidos realizados, se han entregado {pedidos_tardios} pedidos tardíos")
        print("="*50)
        while True:
            opc=input("¿Desea ver un gráfico comparativo de los pedidos tardíos?: ").lower()
            print("="*50)
            if opc in ["si","sí","s"]:
                etiquetas=["Tardíos","No tardíos"]
                tamaños=[pedidos_tardios,pedidos_a_tiempo]
                colores=["darkorange","yellowgreen"]
                plt.pie(tamaños,labels=etiquetas,colors=colores,autopct="%1.1f%%",startangle=100)
                plt.axis("equal")
                plt.title("PEDIDOS")
                plt.show()
                break
            elif opc in ["no","n"]:
                break
            
            
    def mesa_mas_cons(self):
        data_pedidos=pd.read_excel("Pedidos.xlsx")
        mesa_con_consumo= data_pedidos[data_pedidos["pagos"] != 0]
        consumo_por_mesa={}
        for i in mesa_con_consumo.index:
            num_mesa=mesa_con_consumo["num_mesa"][i]
            pago=mesa_con_consumo["pagos"][i]
            if num_mesa in consumo_por_mesa:
                consumo_por_mesa[num_mesa]+=pago
            else:
                consumo_por_mesa[num_mesa] = pago
        imprimir = sorted(consumo_por_mesa.items(),key=lambda x: x[1],reverse=True)
        mesa_mayor, consumo_mayor= imprimir[0]
        
        print(tabulate(imprimir,headers=["MESA","CONSUMO TOTAL"],tablefmt="grid"))

        print("="*60)
        print("LA MESA CON EL MAYOR CONSUMO")
        print("-"*60)
        print(f"Mesa: {mesa_mayor}, con un consumo total de: S/.{consumo_mayor}")
        print("="*60)
        while True:
            opc=input("¿Desea ver un gráfico de las 10 mesas con mayor consumo?: ").lower()
            print("="*50)
            if opc in ["si","sí","s"]:
                mesas=[]
                consumos=[]
                
                for i in range(0,10):
                    mesas.append(str(imprimir[i][0]))
                    consumos.append(imprimir[i][1])
                mesas.reverse()
                consumos.reverse()
                plt.bar(mesas,consumos,color="coral")
                plt.title("TOP 10 MESAS CON MEJORES CONSUMO")
                plt.xlabel("MESAS(N°)")
                plt.ylabel("INGRESOS")
                plt.show()
                break
            elif opc in ["no","n"]:
                break
            
    
    def ingreso_zona(self):
        data_mesas=pd.read_excel("Mesas.xlsx")
        data_pedidos=pd.read_excel("Pedidos.xlsx")
        zona_terrasa= data_mesas[data_mesas["zona_mesa"] != "Sala"]
        zona_sala= data_mesas[data_mesas["zona_mesa"]!="Terraza"]

        terraza_ingreso=0
        sala_ingreso=0
        terraza_mesas=0
        sala_mesas=0
        for i in zona_terrasa.index:
            num_mesa=zona_terrasa["numero_mesa"][i]
            for j in data_pedidos.index:
                if data_pedidos["num_mesa"][j]==num_mesa:
                    terraza_ingreso+=data_pedidos["pagos"][j]
                    terraza_mesas+=1
        for i in zona_sala.index:
            num_mesa=zona_sala["numero_mesa"][i]
            for j in data_pedidos.index:
                if data_pedidos["num_mesa"][j]==num_mesa:
                    sala_ingreso+=data_pedidos["pagos"][j]
                    sala_mesas+=1
        total_ingreso=terraza_ingreso+sala_ingreso
        total_mesas=terraza_mesas+sala_mesas
        porc_terraza=(terraza_ingreso/total_ingreso)*100
        porc_sala=(sala_ingreso/total_ingreso)*100

        imprimir=[[f"Sala",f"S/.{sala_ingreso:.2f}",sala_mesas],[f"Terraza",f"S/.{terraza_ingreso:.2f}",terraza_mesas],["Total",f"S/.{total_ingreso:.2f}",total_mesas]]
        print("\n" + "="*60)
        print(" INGRESOS POR ZONA (SALA VS. TERRAZA) ".center(60))
        print("="*60)
        print(tabulate(imprimir,headers=["Zona", "Ingresos Totales", "Mesas Atendidas"],tablefmt="grid"))
        print("\n" + "ANÁLISIS DE DEMANDA:".center(50))
        print("="*60)
        print(f"- Sala: {porc_sala:.1f}% de los ingresos ({sala_mesas} mesas)")
        print(f"- Terraza: {porc_terraza:.1f}% de los ingresos ({terraza_mesas} mesas)")
        print("="*60)
        while True:
            opc=input("¿Desea ver un gráfico comparativo con los ingresos por cada zona?: ").lower()
            print("="*50)
            if opc in ["si","sí","s"]:
                etiquetas=["Terraza","Sala"]
                tamaños=[terraza_ingreso,sala_ingreso]
                colores=["darkorange","yellowgreen"]
                plt.pie(tamaños,labels=etiquetas,colors=colores,autopct="%1.1f%%",startangle=100)
                plt.axis("equal")
                plt.title("Ingresos por zona")
                plt.show()
                break
            elif opc in ["no","n"]:
                break
#! --------------------------------------------------------------------------------------------------
    def pedidos_dias (self):
        """Función para analizar los pedidos por día de la semana"""
        data_pedidos = pd.read_excel('Pedidos.xlsx')
        dias_pagados = data_pedidos[data_pedidos['pagos'] != 0]
        
        print(dias_pagados)
        
        while True:
           
            fecha = input("Ingrese la fecha (AAAA/MM/DD): ")
            
            try:  
                fecha_f = datetime.strptime(fecha, "%y/%m/%d")
                print(fecha_f)
            except ValueError:
                print("ERROR")    
        
            contador = 0
            for i in data_pedidos.index:
                if str(data_pedidos['fecha'][i])[:10] == fecha:
                        contador += 1
                
            print(f"La cantidad de pedidos en el dia {fecha } es {contador}")
    
    def pago_pedidos_dias (self):
        """Función para analizar los pedidos por día de la semana"""
        data_pedidos = pd.read_excel('Pedidos.xlsx')
        dias_pagados = data_pedidos[data_pedidos['pagos'] != 0]
        
        
        print(dias_pagados)
        while True:
           
            fecha = input("Ingrese la fecha (AAAA/MM/DD): ")
            
            try:  
                fecha_f = datetime.strptime(fecha, "%y/%m/%d")
                print(fecha_f)
            except ValueError:
                print("ERROR")    
        
            contador = 0
            for i in dias_pagados.index:
                if str(dias_pagados['fecha'][i]) [:10] == fecha:
                    contador = dias_pagados['pagos'][i] + contador
                    
                
            print(f"La cantidad de ingresos generados en el dia {fecha } es  s/{round(contador,2)}")
            
    
    
        
    def pedidos_por_intervalo_con_hora(self):
        """Función para contar y mostrar los pedidos en un intervalo de fecha y hora"""
        data_pedidos = pd.read_excel('Pedidos.xlsx')

        # Asegurar que la columna 'fecha' esté en formato datetime
        data_pedidos["fecha"] = pd.to_datetime(data_pedidos["fecha"], format="%Y/%m/%d %H:%M", errors="coerce")

        print("Ingrese el intervalo de fecha y hora para el reporte.")
        print("Formato requerido: AAAA/MM/DD HH:MM (ej. 2025/07/01 15:30)")

        while True:
            try:
                fecha_inicio = input("Fecha y hora de inicio: ")
                fecha_fin = input("Fecha y hora de fin: ")

                inicio = datetime.strptime(fecha_inicio, "%Y/%m/%d %H:%M")
                fin = datetime.strptime(fecha_fin, "%Y/%m/%d %H:%M")

                if inicio > fin:
                    print("La fecha de inicio no puede ser mayor que la fecha de fin.")
                    continue

                # Filtrar los pedidos en el intervalo exacto
                pedidos_filtrados = data_pedidos[
                    (data_pedidos["fecha"] >= inicio) & 
                    (data_pedidos["fecha"] <= fin)
                ]

                cantidad = len(pedidos_filtrados)
                print("-" * 40)
                print(f"Total de pedidos entre {inicio} y {fin}: {cantidad}")
                print("-" * 40)

                # Mostrar tabla resumida de pedidos
                if not pedidos_filtrados.empty:
                    print(pedidos_filtrados[["fecha", "num_mesa", "pedido"]])
                else:
                    print("No se encontraron pedidos en ese intervalo.")
                break

            except ValueError:
                print("❌ Error: Asegúrate de ingresar la fecha en el formato correcto (AAAA/MM/DD HH:MM).")
                
                                                                          
    def entregados_vs_no_e (self):
        """Función para analizar los pedidos entregados vs no entregados"""
        data_pedidos = pd.read_excel('Pedidos.xlsx')
        entregados = data_pedidos[data_pedidos['entregado'] == 'si']
        no_entregados = data_pedidos[data_pedidos['entregado'] == 'no']
        
        cantidad_e = len(entregados)
        cantidad_ne = len(no_entregados)
        
        indices = [cantidad_e, cantidad_ne]
        etiquetas = ['Entregados', 'No Entregados']
        colores = ['green', 'red']
        
        plt.bar(etiquetas, indices,  color=colores)
        plt.title("ENTREGADOS VS NO ENTREGADOS")
        plt.xlabel("Categoría")
        plt.ylabel("Cantidad")
        
        
        for i, valores in enumerate(indices):
            plt.text(i, valores+1, str(valores), ha='center')
        plt.show()
    
    def total_recaudado(self):
        data_pedidos = pd.read_excel('Pedidos.xlsx')
        total_recaudado = 0
        pedidos_pagados = data_pedidos[data_pedidos['pagos'] != 0]
        for i in pedidos_pagados.index:
            total_recaudado = total_recaudado + pedidos_pagados['pagos'][i]
        print("-"*30)
        print(f"El Dinero total recaudado es: {total_recaudado}")
        print("-"*30)                         
        
    def cantidad_productor_por_plato (self):
        data_carta = pd.read_excel('Carta.xlsx')
        
        data_platos = data_carta[data_carta['tipo'] == 'plato']
        print(data_platos)
        data_postres = data_carta[data_carta['tipo'] == 'postre']
        print(data_postres)
        data_bebidas = data_carta[data_carta['tipo'] == 'bebida']
        print(data_bebidas)
        
        indices = ['platos', 'postres', 'bebidas']
        cantidad = [len(data_platos), len(data_postres), len(data_bebidas)]
        colores = ['blue', 'red', 'green']
        plt.bar(indices,cantidad, color=colores)
        plt.title("CANTIDAD DE PRODUCTOS POR PLATO")
        plt.xlabel("TIPO DE PEDIDOS")
        plt.ylabel("CANTIDAD")
        for i, valor in enumerate(cantidad):
            plt.text(i, valor, str(valor), ha='center')
        plt.show()
        
        plt.pie(cantidad, labels=indices, colors=colores, autopct='%1.1f%%', startangle=90)
        plt.show()
        
    def pedidos_por_mesa (self):
        data_pedidos = pd.read_excel('Pedidos.xlsx')
        
        mesa = int(input("ingresar mesa"))
        
        pago_total_de_mesa = 0
        if mesa > 0 and mesa < 50:
            df = data_pedidos[data_pedidos['num_mesa'] == mesa]
            print(df)
            
        for i in df.index:
            pago_total_de_mesa = pago_total_de_mesa + df['pagos'][i]
        print("pago total de mesa: ", pago_total_de_mesa)
        
        for i in df.index:
            pedidos = df['pedido'][i]
            pedidos = ast.literal_eval(pedidos)
            for e in pedidos:
                print(f"pedido: {e['nombre']}, precio: s/. {e['precio']}")
        print("-"*30)
    
    def mozo_mas_pedido (self):
        data_pedidos = pd.read_excel('Pedidos.xlsx')
        data_mozos = pd.read_excel('Mozos.xlsx')
        top = data_pedidos["num_mozo"].value_counts().head(3)
        print(top)
        uno = top.index[0]
        uno_i = top.iloc [0]
        print(uno_i)
        dos = top.index[1]
        dos_i = top.iloc [1]
        tres = top.index[2]
        tres_i = top.iloc [2]

        df_uno = data_mozos[data_mozos['id_mozo'] == uno] 
        print(f"El mozo mas pedido es: {df_uno['nombre'].values[0]} con el id {df_uno['id_mozo'].values[0]}")

        df_dos = data_mozos[data_mozos['id_mozo'] == dos]
        print(f"El 2do mozo mas pedido es: {df_dos['nombre'].values[0]}  con el id {df_dos['id_mozo'].values[0]}")
        
        df_tres = data_mozos[data_mozos['id_mozo'] == tres]
        print(f"El 3er mozo mas pedido es: {df_tres['nombre'].values[0]} con el id {df_tres['id_mozo'].values[0]}")
              
        valores = [uno_i,dos_i,tres_i]
        nombre = [str(top.index[0]), str(top.index[1]), str(top.index[2])]
        color = ["red", "blue", "yellow"]
        
        for i, valor in enumerate(valores):
            plt.text(i,valor, str(valor), ha="center")
        
        plt.bar(nombre, valores, color=color)
        plt.xlabel('ID')
        plt.ylabel('Pedidos')
        plt.title('Mozos con mas pedidos')
        plt.show()


    
    


class Mesas:
    def __init__(self,numeroMesa = 0, zonaMesa =str , capacidad=0, estado_mesa =str):
        self.__numeroMesa = numeroMesa
        self.__zonaMesa = zonaMesa
        self.__capacidad = capacidad
        self.__estado = estado_mesa
        
    @property
    def numeroMesa(self):
        return self.__numeroMesa
    
    @numeroMesa.setter
    def numeroMesa(self, numero):
        self.__numeroMesa = numero
    
    @property
    def zonaMesa(self):
        return self.__zonaMesa
    @property
    def capacidad(self):
        return self.__capacidad
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
      
    
    # Metodos de la clase mesas
    def mostrar_mesas(self):
        df_mesas = pd.read_excel("Mesas.xlsx")
        print(tabulate (df_mesas, headers = "keys", tablefmt = "grid"))

    
    
    def eliminar_mesa (self):
        global data_mesas
        
        while True:
            try:
                numero_mesa = int(input("Ingrese el numero de mesa a eliminar(1 - 50): "))
                if 1<= numero_mesa <= 50:
                    if numero_mesa in data_mesas["numero_mesa"].values:
                        break
                    else:
                        print("La mesa no esta registrada en la base de datos")
                else:
                    print("Error, el numero de mesa esta fuera de rango (50 mesas maximo)")
                    
            except ValueError:
                print("Error en los datos de ingreso")
                
        while True:
            respuesta = input(f"Desea eliminar la mesa numero {numero_mesa} (si/no) ?: ").lower()
            if respuesta in ["si", "no"]:
                break 
            else:
                print("Formato de respuesta incorrecto")
        
        if respuesta == "si":
            
            if numero_mesa in data_mesas["numero_mesa"].values:
                data_mesas = data_mesas[data_mesas["numero_mesa"] != numero_mesa]
                print(f"Mesa con numero {numero_mesa} eliminado correctamente")
                data_mesas.to_excel("Mesas.xlsx", index = False)
                
            else:
                print("La mesa no esta registrada")
        else:
            print("Procedo de eliminacon cancelado")
            
    def liberar_mesas(self):
        if data_mozos.empty:
            print("No hay mozos registrados")
            return
        
        while True:
            idMozo = input("Ingrese el id del mozo (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                 break
            else:
                print("Error, el id del mozo no es correcto")
        
        if idMozo in data_mozos["id_mozo"].astype(str).values:
            mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
            m_reservadas = data_mozos.at[mozo_index, "mesas_reservadas"]
            if isinstance(m_reservadas, str):
                m_reservadas = eval(m_reservadas)
            else:
                m_reservadas = []
            
            if not m_reservadas:
                print("El mozo no tiene mesas asignadas")
                return
            
            print(f"Mesas asignadas al mozo {idMozo}: {m_reservadas}")
            
            while True:
                try:
                    mesa = int(input("Ingrese el número de mesa a eliminar de las asignadas: "))
                    if mesa in m_reservadas:
                        m_reservadas.remove(mesa)
                        data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
                        data_mozos.to_excel("Mozos.xlsx", index=False)
                        print(f"Mesa {mesa} eliminada de las asignaciones del mozo {idMozo}.")
                        
                        
                        # ? ---------------------------------------------------------------------------------
                        # ACTUALIZAR EL ESTADO DEL MOZO A ACTIVO SI TIENE MENOS DE 4 MESAS ASIGNADAS
                        if len(m_reservadas) < 4:
                            data_mozos.at[mozo_index, "estado"] = "Activo"
                            data_mozos.to_excel("Mozos.xlsx", index=False)
                            print(f"El mozo {idMozo} ahora está activo.")
                        # ACTUALIZAR EL ESTADO DE LA MESA A LIBRE
                        data_mesas.loc[data_mesas["numero_mesa"] == mesa, "estado_mesa"] = "Libre"
                        data_mesas.to_excel("Mesas.xlsx", index=False)
                        break
                        # ? ---------------------------------------------------------------------------------
                        
                    else:
                        print("La mesa no está asignada al mozo.")
                except ValueError:
                    print("Debe ingresar un número entero.")
        else:
            print("El id del mozo no está registrado")      
            
class Mozos:
    def __init__(self, idMozo =str, nombre = str, telefono = str,estado = str):
        self.__idMozo = idMozo
        self.__nombre = nombre
        self.__telefono  = telefono
        self.__estado = estado 
        self.__capacidad = 4
    
    @property
    def idMozo(self):
        return self.__idMozo
    @property
    def nombre(self):
        return self.__nombre
    @property
    def telefono(self):
        return self.__telefono
    @property
    def estado (self):
        return self.__estado
    
    @estado.setter
    def estado (self, estado ):
        self.__estado = estado
        
    @property
    def capacidad(self):
        return self.__capacidad
    
    # Metodos de la clase mozos
    def mostrar_mosos(self):
        df_mozos = pd.read_excel("Mozos.xlsx")
        print(tabulate(df_mozos, headers = "keys" , tablefmt = "grid"))
        
        
    def asignar_mozo(self):
        if data_mozos.empty:
            print("No hay mozos registrados")
            return 

        # Validar ID del mozo
        while True:
            idMozo = input("Ingrese el id del mozo a asignar (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                break
            else:
                print("Error, el id del mozo no es correcto")

        # Verificar existencia del mozo
        if idMozo in data_mozos["id_mozo"].astype(str).values:
            mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
            mozo = data_mozos.loc[mozo_index]
        else:
            print("El id del mozo no está registrado")
            return

        # Verificar estado del mozo
        if mozo["estado"] != "Activo":
            print("Error: el mozo no está activo y disponible")
            return

        # Cargar mesas reservadas
        m_reservadas = mozo["mesas_reservadas"]
        if isinstance(m_reservadas, str):
            m_reservadas = eval(m_reservadas)
        else:
            m_reservadas = []

        # Verificar límite de mesas
        if len(m_reservadas) >= 4:
            print("El mozo ya tiene 4 mesas asignadas y ahora está inactivo")
            data_mozos.at[mozo_index, "estado"] = "Inactivo"
            data_mozos.to_excel("Mozos.xlsx", index=False)
            print(f"El mozo {mozo['nombre']} ahora está inactivo.")
            return
        else:
            data_mozos.at[mozo_index, "estado"] = "Activo"
            data_mozos.to_excel("Mozos.xlsx", index=False)
        
        # Asignar mesa
        while True:
            try:
                mesa = int(input("Ingrese el número de mesa a asignar: "))
            except ValueError:
                print("Debe ingresar un número entero")
                continue

            if not (1 <= mesa <= 50):
                print("Error, el número de mesa no es válido (1-100)")
                continue
            
            if str(mesa) not in data_mesas["numero_mesa"].astype(str).values:
                print("El número de mesa no está registrado")
                continue

            if mesa in m_reservadas:
                print("El mozo ya tiene asignada esa mesa, seleccione otra")
                continue

            # Verificar estado de la mesa
            data_mesa = data_mesas[data_mesas["numero_mesa"].astype(str) == str(mesa)]
            if data_mesa.empty:
                print("Error: no hay datos de la mesa")
                continue

            estado_mesa = data_mesa.iloc[0]["estado_mesa"]
            if estado_mesa != "Libre":
                print("La mesa no está libre, seleccione otra")
                continue

            # Todo está correcto, asignar mesa
            m_reservadas.append(mesa)
        
            
        # ?------------------------------------------------------------------------------
            # Actualizar el estado de la mesa a "Reservada"
            data_mesas.loc[data_mesas["numero_mesa"] == mesa, "estado_mesa"] = "Reservada"
            data_mesas.to_excel("Mesas.xlsx", index=False)
        # ?------------------------------------------------------------------------------
        
        
        
            # Actualizar las mesas reservadas del mozo
            data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
            data_mozos.to_excel("Mozos.xlsx", index=False)
            print(f"Mozo {mozo['nombre']} asignado correctamente a la mesa {mesa}.")
            break  



    def cambiar_mozo(self):
        if data_mozos.empty:
            print("No hay mozos registrados")
            return
        
        while True:
            idMozo = input("Ingrese el id del mozo a cambiar (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                break
            else:
                print("Error, el id del mozo no es correcto")
        
        if idMozo in data_mozos["id_mozo"].astype(str).values:
            mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
            m_reservadas = data_mozos.at[mozo_index, "mesas_reservadas"]
            if isinstance(m_reservadas, str):
                m_reservadas = eval(m_reservadas)
            else:
                m_reservadas = []
            
            if not m_reservadas:
                print("El mozo no tiene mesas asignadas")
                return
            
            print(f"Mesas asignadas al mozo {idMozo}: {m_reservadas}")
            
            while True:
                try:
                    mesa = int(input("Ingrese el número de mesa a cambiar: "))
                    if mesa in m_reservadas:
                        nuevo_id_mozo = input("Ingrese el nuevo id del mozo (4 dígitos): ")
                        if len(nuevo_id_mozo) == 4 and nuevo_id_mozo.isdigit():
                            if nuevo_id_mozo in data_mozos["id_mozo"].astype(str).values:
                                nuevo_mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == nuevo_id_mozo].index[0]
                                nuevo_m_reservadas = data_mozos.at[nuevo_mozo_index, "mesas_reservadas"]
                                if isinstance(nuevo_m_reservadas, str):
                                    nuevo_m_reservadas = eval(nuevo_m_reservadas)
                                else:
                                    nuevo_m_reservadas = []
                                
                                # Verificar si el nuevo mozo ya tiene 4 mesas asignadas
                                if len(nuevo_m_reservadas) >= self.capacidad:
                                    print(f"El mozo {nuevo_id_mozo} ya tiene 4 mesas asignadas.")
                                    return
                                
                                # Cambiar la mesa
                                nuevo_m_reservadas.append(mesa)
                                m_reservadas.remove(mesa)
                                data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
                                data_mozos.at[nuevo_mozo_index, "mesas_reservadas"] = str(nuevo_m_reservadas)
                                data_mozos.to_excel("Mozos.xlsx", index=False)
                                print(f"Mesa {mesa} cambiada del mozo {idMozo} al mozo {nuevo_id_mozo}.")
                                break
                            else:
                                print("El nuevo id del mozo no está registrado")
                        else:
                            print("Error, el nuevo id del mozo no es correcto")
                    else:
                        print("La mesa no está asignada al mozo.")
                except ValueError:
                    print("Debe ingresar un número entero.")
    
    
    def eliminar_mozo (self):
        global data_mozos
        # Validar ID del mozo
        while True:
            idMozo = input("Ingrese el id del mozo a eliminar (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                break
            else:
                print("Error, el id del mozo no es correcto")   
        while True:
            respuesta = input(f"Desea eliminar el mozo con id {idMozo} (si/no): ").lower()
            if respuesta in ["si", "no"]:
                break 
            else:
                print("Formato de respuesta incorrecto")
                
        if respuesta == "si":
            # Verificar existencia del mozo
            if idMozo in data_mozos["id_mozo"].astype(str).values:
                data_mozos = data_mozos[data_mozos["id_mozo"].astype(str) != idMozo]
                print(f"Mozo con ID {idMozo} eliminado correctamente.")
                data_mozos.to_excel("Mozos.xlsx", index=False)
            else:
                print("El mozo no esta registrado ")
        else:
            print("Proceso de eliminacion cancelado")
    
    def modificar_datos(self):
        while True:
            idMozo = input("Ingrese el id del mozo a asignar (4 dígitos): ")
            if len(idMozo) != 4 or not idMozo.isdigit():
                print("Error, el id del mozo no es correcto")
                continue

            # Verificar existencia del mozo
            if idMozo in data_mozos["id_mozo"].astype(str).values:
                break
            else:
                print("El id del mozo no está registrado")
                return
        
        mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
        mozo = data_mozos.loc[mozo_index]
        print("-"*80)
        print(f"Datos actuales del mozo {mozo['nombre']}:")
        print(f"ID      : {mozo['id_mozo']}")
        print(f"Nombre  : {mozo['nombre']}")
        print(f"Teléfono: {mozo['telefono']}")
        print(f"Estado  : {mozo['estado']}")
        print("-"*80)
        while True:
            while True:
                print("MENU DE ACTUALIZACION DE DATOS".center(80, "-"))
                print("1. Modificar ID del mozo")
                print("2. Modificar nombre del mozo")
                print("3. Modificar teléfono del mozo")
                print("4. Modificar estado del mozo")
                print("5. Salir")
                opcion = int(input("Seleccione una opción: "))
                if 1 <= opcion <= 5:
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            if opcion == 1:
                nuevo_id = input("Ingrese el nuevo ID del mozo (4 dígitos): ")
                if len(nuevo_id) == 4 and nuevo_id.isdigit():
                    if nuevo_id in data_mozos["id_mozo"].astype(str).values:
                        print("Error, el ID ya está registrado")
                    else:
                        data_mozos.at[mozo_index, "id_mozo"] = nuevo_id
                        data_mozos.to_excel("Mozos.xlsx", index=False)
                        print(f"ID del mozo actualizado a {nuevo_id}.")
                else:
                    print("El ID debe ser de 4 dígitos numéricos.")
            elif opcion == 2:
                nuevo_nombre = input("Ingrese el nuevo nombre del mozo: ")
                contiene_numero = False
                for caracter in nuevo_nombre:
                    if caracter.isdigit():
                        contiene_numero = True
                        print("El nombre no debe tener números")
                        break
                if not contiene_numero:
                    data_mozos.at[mozo_index, "nombre"] = nuevo_nombre
                    data_mozos.to_excel("Mozos.xlsx", index=False)
                    print(f"Nombre del mozo actualizado a {nuevo_nombre}.")
            elif opcion == 3:
                nuevo_telefono = input("Ingrese el nuevo teléfono del mozo (9 dígitos): ")
                if len(nuevo_telefono) == 9 and nuevo_telefono.isdigit():
                    if nuevo_telefono in data_mozos["telefono"].astype(str).values:
                        print("Error, el teléfono ya está registrado")
                    else:
                        data_mozos.at[mozo_index, "telefono"] = nuevo_telefono
                        data_mozos.to_excel("Mozos.xlsx", index=False)
                        print(f"Teléfono del mozo actualizado a {nuevo_telefono}.")
                else:
                    print("El teléfono debe ser de 9 dígitos numéricos.")
            elif opcion == 4:
                nuevo_estado = input("Ingrese el nuevo estado del mozo (Activo/Inactivo): ").title()
                if nuevo_estado in ["Activo", "Inactivo"]:
                    data_mozos.at[mozo_index, "estado"] = nuevo_estado
                    data_mozos.to_excel("Mozos.xlsx", index=False)
                    print(f"Estado del mozo actualizado a {nuevo_estado}.")
                else:
                    print("El estado debe ser 'Activo' o 'Inactivo'.")
            elif opcion == 5:
                print("Saliendo del menú de actualización de datos.")
                break
            
class Pedidos:
    def __init__(self, num_mesa=None, num_mozo=None, pedido=None, fecha=str, fecha_en= str, entregado=str, pagos = 0):
        self.__num_mesa = num_mesa
        self.__num_mozo = num_mozo
        self.__pedido = pedido
        self.__fecha = fecha
        self.__fecha_en = fecha_en
        self.__entregado = entregado
        self.__pagos = pagos
        
    @property
    def num_mesa (self):
        return self.__num_mesa
    
    @num_mesa.setter
    def num_mesa (self, num_mesa):
        self.__num_mesa = num_mesa
        
    @property
    def num_mozo (self):
        return self.__num_mozo
    
    @num_mozo.setter
    def num_mozo (self, num_mozo):
        self.__num_mozo = num_mozo
    
    @property
    def pedido(self):
        return self.__pedido 
        
    @property
    def fecha (self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
    
    @property
    def fecha_en (self):
        return self.__fecha_en
    @fecha_en.setter
    def fecha_en (self, fecha_en):
        self.__fecha_en = fecha_en
    
    @property
    def entregado (self):
        return self.__entregado
    @property
    def pagos (self):
        return self.__pagos
    
         
    def mostrar_pedidos(self):
        
        df_pedidos = pd.read_excel("Pedidos.xlsx")
        
        def nombre_precio (pedidos_str):
            try:
                # ast.literal_eval(pedidos_str) -> HACE QUE UNA CADENA DE TEXTO SE VUELVA EN UNA LISTA DE DICCIONARIOS
                pedidos = ast.literal_eval(pedidos_str)
                if isinstance(pedidos, list):
                    nombre_precio = []
                    for e in pedidos:
                        nombre_precio.append(f"{e['nombre']} (S/ {e['precio']})")
                    return ", ".join(nombre_precio)  #JOIN, une los elementos de una lista en una sola cadena de texto
                return ""
            except Exception:
                return ""
        
        df_pedidos["pedido"] = df_pedidos["pedido"].apply(nombre_precio)
        # Seleccionar solo las columnas requeridas
        columnas = ["num_mesa", "num_mozo", "pedido", "fecha", "fecha_en", "entregado", "pagos"]
        print(tabulate(df_pedidos[columnas], headers="keys", tablefmt="grid"))

class Pago:
    def __init__(self, Idmesa=0, pagoF=0):
        self.__Idmesa=Idmesa
        self.__pagoF=pagoF
    
    @property
    def Idmesa(self):
        return self.__Idmesa
    @property
    def pagoF(self):
        return self.__pagoF
    
    
class Carta:
    def __init__(self,idCarta=0,nombre=str,tipo=str,precio=0):
        self.__idCarta=idCarta
        self.__nombre=nombre
        self.__tipo=tipo
        self.__precio=precio
        
    @property
    def idCarta(self):
        return self.__idCarta
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        self.__precio=nuevo_precio

                    
def menu():
    print("--" * 30)
    print("<< MENU PRINCIPAL >>".center(60))
    print("--" * 30)
    print("[1] Registrar mesa y mozo    ") 
    print("[2] Solicitar mozo           ")
    print("[3] Ver carta                ")
    print("[4] Tomar pedido             ")
    print("[5] Modificar pedido         ")
    print("[6] Finalizar pedido         ")
    print("[7] Calcular pago            ")
    print("[8] Ver reportes             ")
    print("[0] Salir                    ")

    print("--" * 30)
    print("<< ...SISTEMA RESTAURANTE -- BIENVENIDOS ...>>".center(60))
    
    print("--" * 30)



def caratula():
    print("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@  ".center(80))
    print("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@  ".center(80))
    print("  @@   @@   @@    @@   @@   @@  ".center(80))
    print(" @@    @@   @@    @@   @@    @@ ".center(80))
    print("@@@   @@    @@    @@    @@   @@@".center(80))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@".center(80))
    print("@@   @@@    @@    @@    @@@   @@".center(80))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@".center(80))
    print(" @@@@@@@@@@@@@ @@  @@@@@@   @@@ ".center(80))
    print(" @@@@@@@@@@@@@@  @@@@@@@@@@  @@ ".center(80))
    print(" @@@@       @@@  @@@@@ @@@@  @@ ".center(80))
    print(" @@@@       @@@  @@@@@@@@@@  @@ ".center(80))
    print(" @@@@      @@@@    @@@@@@@   @@ ".center(80))
    print(" @@@@      @@@@@@@@@@@@@@@@@@@@ ".center(80))
    print(" @@@@       @@@@@@@@@@@@@@@@@@@ ".center(80))
    print(" @@@@       @@@              @@ ".center(80))
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ".center(80))
    print("================================".center(80))
    print("SISTEMA DE GESTIÓN DE PEDIDOS PARA RESTAURANTES".center(80))
    print("TRABAJO FINAL".center(80))
    print("================================".center(80))
    print("Curso: PROGRAMACION ORIENTADO A OBJETOS".center(80))
    print("Docente: Juan Alfonso Ramírez Espinoza".center(80))
    print("2025-1".center(80))
    print("--------------------------------".center(80))
    print("Integrantes:".center(80))
    print("Hidalgo Martel, Joseph Edward (U202421665)".center(80))
    print("Huamán Flores, Alexis Miguel (U20241G114)".center(80))
    print("Peña Roña, Antony Yomar (U202421102)".center(80))
    print("Villavicencio Davila, Ivette Lucero (U20241G010)".center(80))
    print("================================".center(80))
    print("LOS DINOSAURIOS".center(80))
    print("================================".center(80))


def main():
    mesas = Mesas ()
    mozos = Mozos()
    pedidos = Pedidos()
    restaurante = Restaurante(mozos,mesas)
    caratula()
    while True:
        menu()
        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if 0 <= opcion <= 8:
                    break
                else:
                    print("Opción invalida. Intente nuevamente.")
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero.") 
        
        if opcion == 0:
            print("Saliendo del sistema...")
            break
          
        if opcion == 1:
        # ?------------------------------------------------------------------------------
            
            while True:
                print("----------------------------------------")
                print("1. Registrar mesas")
                print("2. Registrar mozos")
                print("3. Reportes de registros mesas por zona")
                print("4. Reportes de registros mozos")
                print("5. Eliminar mozos")
                print("6. Eliminar mesas")
                print("7. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if 1 <= subopcion <= 7:
                        if subopcion == 1:   
                            restaurante.registrar_mesas()
                        elif subopcion == 2:
                            restaurante.registrar_mozos()
                        elif subopcion == 3:
                            restaurante.r_registros()
                        elif subopcion == 4:
                            restaurante.reporte_mozos()
                        elif subopcion == 5:
                            mozos.eliminar_mozo()
                        elif subopcion == 6:
                            mesas.eliminar_mesa()
                        elif subopcion == 7:
                            break
                        else:
                            print("Opcion invalida. Intente nuevamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
        # ?------------------------------------------------------------------------------
            
            
            
            
            
        elif opcion == 2:  # Asignar mozo a mesa
            while True:
                print("----------------------------------------")
                print("1. Asignar mozo a mesa")
                print("2. Cambiar mozo de la mesa actual")
                print("3. Eliminar mesa asignada")
                print("4. Modificar datos del mozo")
                print("5. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if subopcion == 1:
                       mozos.asignar_mozo()
                    elif subopcion == 2:
                        mozos.cambiar_mozo()
                    elif subopcion == 3:
                        mesas.liberar_mesas()
                    elif subopcion == 4:
                        mozos.modificar_datos()
                    elif subopcion == 5:
                        print("Saliendo del menú de mozos.")
                        break  # Salimos del bucle porque eligió salir
                    else:
                        print("Opción invalida. Intente nuevamente.")
                        
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
        
        elif opcion == 3:
            while True:
                print("[1] Agregar carta")
                print("[2] Modificar carta")
                print("[3] Eliminar carta")
                print("[4] Listar carta")
                print("[5] Salir")

                subopcion = input("Seleccione la opcion ( 0 salir): ")
                if subopcion == "1":
                    restaurante.agregar_carta()
                elif subopcion == "2":
                    restaurante.modificar_carta()
                elif subopcion == "3":
                    restaurante.eliminar_carta()
                elif subopcion == "4":
                    restaurante.mostrar_carta()
                elif subopcion == "5":
                    break
                else:
                    print("Opcion no valida. Por favor, intente nuevamente.")
                    
        elif opcion == 4:
            while True:
                print("----------------------------------------")
                print("1. Realizar el pedido")
                print("2. Reporte de cuantos clientes tienen su pedido")
                print("3. Salir")   
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if subopcion == 1:
                        restaurante.r_pedidos()
                    elif subopcion == 2:
                        restaurante.reportes_pedidos()
                    elif subopcion == 3:
                        print("Saliendo del menú de Pedidos.")
                        break  # Salimos del bucle porque eligió salir
                    else:
                        print("Opción invalida. Intente nuevamente.")
                        
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
                
        elif opcion == 5:
                print("<< MODIFICAR PEDIDO >>".center(30))
                print("-"*30)
                restaurante.modificar_pedido()

        elif opcion ==6 :
                print("<< FINALIZAR PEDIDO >>".center(30))
                print("-"*30)
                restaurante.finalizar_pedido()        
                
        elif opcion==7:
                restaurante.realizar_pago()
        
        elif opcion == 8: # Aqui se muestran los reportes de los mozos , mesas y los pedidos de los clientes
            while True:
                print("[1]. Mostrar mesas")
                print("[2]. Mostrar mozos")
                print("[3]. Mostrar pedidos clientes")
                print("[4]. Mostrar mozo con mas pedidos")
                print("[5]. Mostrar promedio tiempo espera")
                print("[6]. Pedidos tardios")
                print("[7]. Mostrar mesa mayor consumo")
                print("[8]. Mostrar ingresos por zona (sala/Terrasa")
                print("[9]. MAS REPORTES")
                print("[0]. salir")
                try:
                    subopcion = int(input("Seleccione una opcion ( 0 salir ): "))
                    if subopcion == 0:
                        break
                    elif subopcion == 1:
                        mesas.mostrar_mesas()
                    elif subopcion == 2:
                        mozos.mostrar_mosos()
                    elif subopcion == 3:
                        pedidos.mostrar_pedidos()
                    elif subopcion == 4:
                        restaurante.mozo_mas_pedido()
                    elif subopcion == 5:
                        restaurante.prom_tiempo_e()
                    elif subopcion == 6:
                        restaurante.pedidos_tardes()
                    elif subopcion == 7:
                        restaurante.mesa_mas_cons()
                    elif subopcion == 8:
                        restaurante.ingreso_zona()
                        
                        
                    elif subopcion == 9:
                        while True:
                            print("[1]. entregados_vs_no_e")
                            print("[2]. TOTAL RECAUDADO")
                            print("[3]. CANTIDAD DE PRODUCTOS POR PLATO")
                            print("[4]. PEDIDOS POR DIA")
                            print("[5]. PEDIDOS POR MESA")
                            print("[6]. MOZO MAS PEDIDO")
                            print("[7]. pedidos_por_intervalo_con_hora")
                            print("[8]. pago_pedidos_dias")
                            print("[0]. SALIR")
                            try:
                                subopcion = int(input("Seleccione una opcion ( 0 salir ): "))
                                if subopcion == 0:
                                    break
                                elif subopcion == 1:
                                    restaurante.entregados_vs_no_e()
                                
                                elif subopcion == 2:
                                    restaurante.total_recaudado()
                                
                                elif subopcion == 3:
                                    restaurante.cantidad_productor_por_plato()
                                
                                elif subopcion == 4:
                                    restaurante.pedidos_dias()
                                    
                                elif subopcion == 5:
                                    restaurante.pedidos_por_mesa()
                                    
                                elif subopcion == 6:
                                    restaurante.mozo_mas_pedido()
                                    
                                elif subopcion == 7:
                                    restaurante.pedidos_por_intervalo_con_hora()
                                    
                                elif subopcion == 8:
                                    restaurante.pago_pedidos_dias()
                            except ValueError:
                                print("Entrada invalida. Por favor, ingrese un numero.")
                        
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")

main()