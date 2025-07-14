import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

encabezados = ['sepallength','sepalwidth','petallength','petalwidth','species']
df = pf.read_csv('zoo.csv', sep=";")
df = pd.read_csv('iris.csv', names=encabezados, header=None)

df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
print(df_a)

#GUARDAR Y AGREGAR
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

# df_rango = df_a[(df_a['Especie'] == especie)]

#encabezados= ['mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt', 'drinks', 'selector']
#        self.__data = pd.DataFrame(data, columns=encabezados)

def animales_por_rango_fecha(self):
        df_a = pd.read_excel('zoologico.xlsx', sheet_name='animales')
        fecha_1 = input("Fecha_ 1 = (DD/MM/AAAA): ").strip()
        fecha_2 = input("Fecha_ 2 = (DD/MM/AAAA): ").strip()
        
        data_rango = df_a[(df_a['Fecha ingreso']>= fecha_1) & (df_a['Fecha ingreso']<= fecha_2)]
        if data_rango.empty:
            print("No hay datos para la fecha ingresada")
        else:
            print(data_rango)    
            
#nan
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
#BUSCAR PARA SUMAR
#df_sum_total = df.groupby('Tipo de Entrada')['Total Venta'].sum().reset_index()
#GUARDAR
# df_sum_total.to_csv('Total de Ventas Por Clase', index=False) 

#plt.bar(nombre,valores,color=)
#plt.pie(cantidad, labels=titulos, autopct='%1.1f%%', startangle=140)
#plt.scatter(bajas, altas, color="r" , marker="o")
#plt.plot(años,lista, marker='o', color='blue')

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
        
    def agregar_columna(self):
        self.__df['EsMayorDeEdad'] = self.__df['Age'] >= 18
        print(self.__df[['Name', 'Age', 'EsMayorDeEdad']].head())