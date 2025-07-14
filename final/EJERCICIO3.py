import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Data:
    def __init__(self, data):
        encabezados= ['mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt', 'drinks', 'selector']
        self.__data = pd.DataFrame(data, columns=encabezados)
    
    @property
    def data(self):
        return self.__data
    
    def leer(self):
        print(self.__data)
        
    def operaciones(self):
        
        media = self.__data['alkphos'].mean()
        #mediana
        mediana = self.__data['alkphos'].median()
        #moda
        moda = self.__data['alkphos'].mode()
        print("-"*40)
        print(f"Para la columna alkphos la media es {media}")
        print(f"Para la columna alkphos la mediana es {mediana}")
        print(f"Para la columna alkphos la moda es \n{moda}")
        print("-"*40)
    def Nan (self):
        
        data_copia= self.__data.copy()

        filas = data_copia.shape[0]
        columnas = data_copia.shape[1]
        print(f"El dataframe tiene {filas} filas y {columnas} columnas")
        
        for i in range(50):
            f = np.random.randint(0, filas)
            c = np.random.randint(0, columnas)
            data_copia.iloc[f, c] = np.nan
            
        return data_copia

    def Contar_nan (self):
        data_copia = self.Nan()
        print(data_copia)
        
        for e in data_copia.columns:
            print(f"La columna {e} tiene {data_copia[e].isna().sum()} nan")
        
    def eliminar_nan (self):
        data_copia = self.Nan()
        #print(data_copia)
        df = data_copia.dropna()
        print(df)
        

data1 = [
            [85, 92, 45, 31, 58, 3, 1],
            [90, 94, 41, 32, 67, 5, 2],
            [80, 88, 38, 33, 45, 2, 1],
            [85, 92, 45, 31, 58, 3, 1],
            [90, 94, 41, 32, 67, 5, 2],
            [80, 88, 38, 33, 45, 2, 1],
            [85, 92, 45, 31, 58, 3, 1],
            [90, 94, 41, 32, 67, 5, 2],
            [80, 88, 38, 33, 45, 2, 1],
            [85, 92, 45, 31, 58, 3, 1],
            [90, 94, 41, 32, 67, 5, 2],
            [80, 88, 38, 33, 45, 2, 1],
        ]
       
data = Data(data1)

data.eliminar_nan()
