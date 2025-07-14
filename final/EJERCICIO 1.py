import pandas as pd
import matplotlib.pyplot as plt

class Data:
    def __init__(self):
        pass
    def leer_data(self):
        df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
        print(df_a)
        
        df_z = pd.read_excel('zoologico.xlsx', sheet_name='zonas')
        print(df_z)
        
    def animal_con_mas_visitas(self):
        df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
        max = df_a['Visitas'].max()
        print(f"MAXIMO: {max}")
        
        for e in range(len(df_a)):
            data = df_a.iloc[e]
            if data['Visitas'] == max:
                print(data['Nombre'])
                print(data['Especie'])
                print(data['Visitas'])
                print("-"*30)
    
    def especio_especifica(self, especie):    
        df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
        lista_df= []
        
        df_rango = df_a[(df_a['Especie'] == especie)]
        print(df_rango)
        """
        for i in range(len(df_a)):
            data = df_a.iloc[i]
            if data['Especie'] == especie:
                lista_df.append(data)
        
        df_listada = pd.DataFrame(lista_df)
        print(df_listada)
        """
        
    def animales_por_rango_fecha(self):
        df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
        fecha_1 = input("Fecha_ 1 = (DD/MM/AAAA): ").strip()
        fecha_2 = input("Fecha_ 2 = (DD/MM/AAAA): ").strip()
        
        data_rango = df_a[(df_a['Fecha ingreso']>= fecha_1) & (df_a['Fecha ingreso']<= fecha_2)]
        if data_rango.empty:
            print("No hay datos para la fecha ingresada")
        else:
            print(data_rango)
        
    def animales_zona(self):
        df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
        df_z = pd.read_excel('zoologico.xlsx', sheet_name='zonas')
        
        zona = input("Zona: ").strip()
        
        df_rango = df_a[(df_a['Zona'] == zona)]
        if df_rango.empty:
            print("No hay nada")
        else:
            print(df_rango)
    
    def grafico_1(self):
        df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
        df_m = df_a[(df_a['Zona'] == 'Mamiferos')]
        df_av = df_a[(df_a['Zona'] == 'Aves')]
        df_ac = df_a[(df_a['Zona'] == 'Acuaticos')]
        cantidad_n = len(df_m)
        cantidad_av = len(df_av)
        cantidad_ac = len(df_ac)
        
        num = [cantidad_n, cantidad_av, cantidad_ac]
        nombres = ['Mamiferos', 'Aves', 'Acuaticos']
        color = ['blue', 'red', 'yellow']
        
        plt.bar(nombres,num, color=color) 
        
        plt.show()
        
    
        
def menu():
    print ("BIENVENIDOS")
    print ("1. LEER")
    print ("2. Animal con mas visitas")
    print ("3. Animales por ESPECIE")
    print ("4. Animales por rango de fecha")
    print ("5. Animales por zona")
    print ("6. Grafico 1")
    
    print ("0. Salir")
    
def main():
    data = Data()
    while True:
        try:
            menu()
            opcion = int(input("Ingresar opcion: "))
            if opcion == 1:
                data.leer_data()
            elif opcion == 2:
                data.animal_con_mas_visitas()
            elif opcion == 3:
                especie = input("Ingrese la especie: ")
                data.especio_especifica(especie)
            elif opcion == 4:
                data.animales_por_rango_fecha()
            elif opcion == 5:
                data.animales_zona()
            elif opcion == 6:
                data.grafico_1()
            elif opcion == 0:
                break
            
            
        except ValueError:
            print("error")
    
    
    
main()