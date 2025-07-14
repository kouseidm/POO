import pandas as pd
import matplotlib.pyplot as plt

class Data:
    def __init__(self):
        self.__data = pd.read_excel('perdidas.xlsx') 
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    
    def leer(self):
        print(self.__data)
        
        
    def grafico (self):
        df = self.__data
        df_movistar = df[(df['Empresa'] == 'Movistar')]
        
        años = df_movistar['Periodo']
        lista = df_movistar['Perdidas'].str.replace('%','').astype(float)
        
        plt.plot(años,lista, marker='o', color='blue')
        plt.xlabel("AÑOS")
        plt.ylabel("GANANCIA")
        plt.title("GANANCIA DE MOVISTAR EN EL PERIODO DE AÑOS")
        plt.show()
        
    def scatter(self):
        df = self.__data
        altas = df['Altas']
        bajas = df['Bajas']
        plt.scatter(bajas, altas, color="r" , marker="o")
        plt.title("Relación entre las altas y bajas en general")
        plt.xlabel("BAJAS")
        plt.ylabel("ALTAS")
        plt.show()
        
    def agregar_nuevo(self):
        
        codigo = input("CODIGO: ")
        empresa = input("EMPRESAS: ")
        periodo = input ("PERIODO: ")
        altas = int(input("ALTAS: "))
        bajas = int(input("BAJAS: "))
        perdida = (bajas / altas)*100
        perdida = round(perdida, 2)
        perdida = f"{perdida}%"
        
        nuevo = {
            "Codigo": codigo,
            "Empresa": empresa,
            "Periodo": periodo,
            "Altas": altas,
            "Bajas": bajas,
            "Perdidas": perdida
        } 
        
        self.__data = pd.concat([self.__data, pd.DataFrame([nuevo])], ignore_index=True)
        self.__data.to_excel('perdidas.xlsx', index=False)
        print ( self.__data)
        
data = Data()


data.agregar_nuevo()