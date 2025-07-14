import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Dataframe:
    def __init__(self):
        pass
    
    def leer_dataframe(self):
        df = pd.read_csv('iris.csv')
        print(df)
        
    def encabezados (self):
        encabezados = ['sepallength','sepalwidth','petallength','petalwidth','species']
        df = pd.read_csv('iris.csv', names=encabezados, header=None)
        print(df)
    
    def operaciones_1era (self):
        encabezados = ['sepallength','sepalwidth','petallength','petalwidth','species']
        df = pd.read_csv('iris.csv', names=encabezados, header=None)
        df = df['sepallength']
        print("----------MEDIA----------")
        print(df.mean())
        print("----------MEDIANA----------")
        print(df.median())
        print("----------MODA----------")
        print(df.mode())
        print("----------MAX----------")
        print(df.max())
        print("----------MIN----------")
        print(df.min())
    
    def ordenar_df(self):
        encabezados = ['sepallength','sepalwidth','petallength','petalwidth','species']
        df = pd.read_csv('iris.csv', names=encabezados, header=None)
        print("----------------ASCENDENTE------------------")
        asc = df.sort_values(by='sepalwidth')
        print(asc)
        asc = asc['sepalwidth'].sort_values()
        print(asc)
        
        print("----------------ASCENDENTE------------------")
        des = df.sort_values(by= 'petallength',ascending=False)
        print(des)
        des = des['petallength']
        print(des)
    
    def resumir_specias(self):
        encabezados = ['sepallength','sepalwidth','petallength','petalwidth','species']
        df = pd.read_csv('iris.csv', names=encabezados, header=None)

        resum = df['species']
        print(resum)
        print(resum.describe())
        
    def diagrama_4 (self):
        encabezados = ['sepallength','sepalwidth','petallength','petalwidth','species']
        df = pd.read_csv('iris.csv', names=encabezados, header=None)
        
        df_4 = df[['sepallength','sepalwidth','petallength','petalwidth']]
        print("DESCRIPCION")
        print(df_4.describe())
        plt.boxplot(df_4)
        
        plt.title("DIAGRAMA PARA 4 ATRIBUTOS")
        plt.ylabel('Longitud (cm)')
        plt.show()
    
    def diagrama_5 (self):
        encabezados = ['sepallength','sepalwidth','petallength','petalwidth','species']
        df = pd.read_csv('iris.csv', names=encabezados, header=None)
        print("DESCRIPCION")
        print(df.describe())
        sns.pairplot(df, hue='species')
        plt.suptitle("Relaciones entre atributos por especie")
        plt.show()
        
       
        

def menu():
    print("Bienvenidos")
    print("1. leer")
    print("2. encabezados")
    print("3. operaciones_1era")
    print("4. ordenar_df")
    print("5. resumir_specias")
    print("6. diagrama_4")
    print("7. diagrama_5")
    print("0. Salir")
    
data = Dataframe()
def main():
    while True:
        try:
            menu()
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                data.leer_dataframe()
            elif opcion == 2:
                data.encabezados()
            elif opcion == 3:
                data.operaciones_1era()
            elif opcion == 4:
                data.ordenar_df()
            elif opcion == 5:
                data.resumir_specias()
            elif opcion == 6:
                data.diagrama_4()
            elif opcion == 7:
                data.diagrama_5()
            elif opcion == 0:
                break
        except ValueError:
            print("Error")
main()