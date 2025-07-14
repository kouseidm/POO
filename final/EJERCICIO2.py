import pandas as pd
import matplotlib.pyplot as plt

class Data :
    def __init__(self):
        pass
    def leer(self):
        df = pd.read_excel('entradas.xlsx')
        print(df)
    def mostraR_ventas_edad(self):
        df = pd.read_excel('entradas.xlsx')
        
        df_sum_por_edad = df.groupby('Edad')['Cantidad'].sum().reset_index()
        print(df_sum_por_edad)
        
        
       
    def grafico_1(self):
        df=pd.read_excel('entradas.xlsx')
        #grafico pie, de total de entradas ventidas por edad
        df_sum_por_edad = df.groupby('Edad')['Cantidad'].sum().reset_index()
        edades = df_sum_por_edad['Edad']
        cantidad = df_sum_por_edad['Cantidad']
        plt.pie(cantidad, labels=edades, autopct='%1.1f%%', startangle=140)
        plt.legend()
        plt.title("GRAFICO DE CANTIDAD DE VENTAS POR EDAD")
        plt.axis('equal')
        plt.show()
        
    
    def total_entradas_tipo(self):
        df = pd.read_excel('entradas.xlsx')
        
        df_adulto = df[(df['Tipo de Entrada'] == 'Adulto')]
        df_estudiante = df[(df['Tipo de Entrada'] == 'Estudiante')]
        df_niño = df[(df['Tipo de Entrada'] == 'Niño')]
        
        sum_adulto = 0
        for i in range(len(df_adulto)):
            sum_adulto += df_adulto.iloc[i]['Total Venta']
        #print(f'El total de ventas de Adulto es {sum_adulto}')
        sum_estudiante = 0
        for i in range(len(df_estudiante)):
            sum_estudiante += df_estudiante.iloc[i]['Total Venta']
        #print(f'El total de ventas de Estudiante es {sum_estudiante}')
        sum_niño = 0
        for i in range(len(df_niño)):
            sum_niño += df_niño.iloc[i]['Total Venta']
        #print(f'El total de ventas de Niño es {sum_niño}')
        
        df_sum_total = df.groupby('Tipo de Entrada')['Total Venta'].sum().reset_index()
        print(df_sum_total)
        
        df_sum_total.to_csv('Total de Ventas Por Clase', index=False) 
        
        
        
def menu():
    print("BIENVENIDO")
    print("1. Leer datos")
    
def main():
    data = Data()
    try:
        while True:
            menu()
            opcion = int(input("INGRESE OPCIÓN: "))
            if opcion == 1:
                data.leer()
            elif opcion == 2:
                data.mostraR_ventas_edad()
            elif opcion == 3:
                data.grafico_1()
            elif opcion == 4:
                data.total_entradas_tipo()
            elif opcion == 0:
                break
                
        
    except ValueError:
        print("ERROR")
    
main()