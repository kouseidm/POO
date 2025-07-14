import pandas as pd
import matplotlib.pyplot as plt

class Data(): 
    def __init__(self):
        self.__df = pd.read_csv('titanic.csv', sep=";")
    
    def leer(self):
        df = self.__df
        print(df)
        
    def descripciones (self):
        df = self.__df
        filas = df.shape[0]
        columnas = df.shape[1]
        
        print(f"El dataframe tiene {filas} filas y {columnas} columnas")
        
        print(f"num de datos: {df.size}")
        
        #columnas
        print(df.columns)
        #filas
        print(df.index) 
        print("="*30)
        print(df.dtypes)
        
        print("PRIMERAS 10 COLUMNAS")
        print(df.head(10))
        print("-"*30)
        print("ULTIMAS 10 COLUMNAS")
        print(df.tail(10))
        
    def identificador(self):
        df = self.__df
        df = df[(df['PassengerId'] == 148)]
        print(df)
        
    def filas_pares(self):
        df = self.__df
        
        df = df.iloc[::2]
        print(df)
        
    def nombres_alfa(self):
        df = self.__df
        df_1 = df[(df['Pclass'] == 1)]
        
        df_ordenado = df_1.sort_values(by='Name')
        nombres = df_ordenado['Name']
        print(nombres)
    
    def porc_sup_clase(self):
        df = self.__df
  
        df_supervivientes = df.groupby('Pclass')['Survived'].sum()
        df_total = df.groupby('Pclass').size()
    
        porcentaje = (df_supervivientes / df_total) * 100
        for clase, porcentaje in porcentaje.items():
            print(f"Clase {clase}: {porcentaje:.2f}%")
        
        print(porcentaje)
        print("TOTAL")
        print(df_total)
        print("SUPERVIVIENTES")
        print(df_supervivientes)
        
    def eliminar_edad_nan(self):
        df_copia = self.__df
        
        df_copia = df_copia.dropna(subset='Age')
        print(df_copia) 
        
    def edad_mujeres(self):
        
        df = self.__df
        df_mu = df[(df['Sex'] == 'female')]

        print("MEDIA")
        df_mu = df_mu.groupby('Pclass')['Age'].median()
        print(df_mu)
    
    
    
def main():
    data = Data()
    while True:
        opcion = int(input("INGRESAR OPCION: "))
        if opcion == 0:
            break
        elif opcion == 1:
            data.leer()
            
        elif opcion == 2:
            data.descripciones()
            
        elif opcion == 3:
            data.identificador()
            
        elif opcion == 4:
            data.filas_pares()
            
        elif opcion == 5:
            data.nombres_alfa()
            
        elif opcion == 6:
            data.porc_sup_clase()
            
        elif opcion == 7:
            data.eliminar_edad_nan()
            
        elif opcion == 8:
            data.edad_mujeres()



main()