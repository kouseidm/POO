import pandas as pd
import matplotlib.pyplot as plt

class Data:
    def __init__ (self):
        pass
    

    def mostrar_df (self):
        df = pd.read_csv('ejemplo.csv', sep=';')
        print(df)
    
    def listar_mesas(self):
        df = pd.read_csv('ejemplo.csv', sep=';')
        for i in range(len(df)):
            df_m= df.iloc[i]
            print(f"Mes: {df_m['mes']}")
            print(f"Balance = {df_m['ventas']} - {df_m['gastos']} = {df_m['ventas']-df_m['gastos']}")
            print("-"*60)
            
        print("VENDAS TOTALES")
        df_ventas = df['ventas']
        suma = df['ventas'].sum()
        print("summa", suma)
        
        print("GASTOS TOTALES")
        df_gastos = df['gastos']
        suma = df['gastos'].sum()
        print("summa", suma)
        
        colores = ['b','r']
        df_gastos = df['mes']
        plt.plot (df_gastos, df_ventas, color = colores[0], label = 'mes')
        plt.legend()
        plt.title("TABLA DE GASTOS- VENTAS")
        plt.xlabel("GASTOS")
        plt.ylabel("VENTAS")
        plt.show()
    
    
def menu():
    print("BIENVENIDO")
    print("1. MOSTRAR DATA")
    print("2. LISTAR MESA")

def main():
    try:
        while True:
            menu()
            opcion = input("INGRESE OPCIÓN: ")
            if opcion == "1":
                data = Data()
                data.mostrar_df()
            elif opcion == '2':
                data = Data()
                data.listar_mesas()
          
    except ValueError:
        print("Error")
main()