
# Importaciones
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np 
from IPython.display import display

# Imputación de nulos
# -----------------------------------------------------------------------
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

##FUNCIONES DE EXPLORACION##

def exploracion_general (lista):
    """Esta función proporciona toda la informacion necesaria de uno o varios DataFrame
    
    Args:
    lista : lista de los DataFrame que queremos explorar
    
    Returns:
    La funcion no tiene return pero devuelve varios prints con
    la informacion que necesitamos:
    - Descripciones separadas por columnas numericas y categoricas
    - Tipos de dato por columna
    - Numero total de filas y columnas
    - Informacion adicional
    - Total de nulos
    - Total de duplicados"""


    for df in lista:

        print("------Exploracion del dataframe: {} ------".format(df.name))
        try:
            print("-------Descripción columnas numéricas:---------")
            print(df.describe())
        except:
            print("Este DataFrame no contiene columnas numericas")

        try:
            print("-------Descripción columnas categoricas:---------")
            print(df.describe(include="O"))
        except: 
            print("Este DataFrame no contiene columnas categoricas")

        print("------Tipos de datos:---------")
        print(df.dtypes)
        print("------Numero de filas y columnas:------")
        print(df.shape)
        print("------Información adicional:---------")
        print(df.info())
        print("------Cantidad de nulos:---------")
        print(df.isnull().sum())
        print("------Cantidad de duplicados:---------")
        print(df.duplicated().sum())
    
def exploracion_columna (lista):

    """Esta función proporciona toda la informacion necesaria de cada columna del DataFrame
    
    Args:
    lista : lista de los DataFrame que queremos explorar
    
    Returns:
    La funcion no tiene return pero devuelve varios prints con
    la informacion que necesitamos:
    - Frecuencia de cada valor unico de la columna
    - Total de nulos
    - Total de duplicados"""

    for dataframe in lista:
        print("------Exploracion del dataframe: {} ------".format(dataframe.name))
        for columna in list(dataframe.columns):
            print(f" \n----------- ESTAMOS ANALIZANDO LA COLUMNA: '{columna.upper()}' -----------\n")
            print(f"* Frecuencia de valores en la columna: \n {dataframe[columna].value_counts()}")
            print(f"La suma de datos nulos {dataframe[columna].isnull().sum()}")
            print(f"La suma de datos duplicados {dataframe[columna].duplicated().sum()}")
            
def graficos_hisp (dataframe, lista_col):

    """Esta función crea graficos histplot para las columnas y el dataframe indicados
    
    Args:
    dataframe : DF que contiene las columnas que queremos analizar
    lista_col : lista de columnas que queremos analizar del DF anterior
    
    Returns:
    La funcion devuelve un grafico histplot por cada columna indicada
    en la lista"""

    fig, axes = plt.subplots(len(lista_col), 1, figsize=(30,20))

    axes = axes.flat

    for indice, columna in enumerate(lista_col):

        sns.histplot(x = columna, data = dataframe, color = "purple", kde = True, bins = 15, ax=axes[indice])
        axes[indice].set_title(columna)
        axes[indice].set_xlabel("Frecuencia")
        plt.gca().spines[["top", "right"]].set_visible(False)

        fig.tight_layout();

def graficos_boxp (dataframe, lista_col):

    """Esta función crea graficos boxplot para las columnas y el dataframe indicados
    
    Args:
    dataframe : DF que contiene las columnas que queremos analizar
    lista_col : lista de columnas que queremos analizar del DF anterior
    
    Returns:
    La funcion devuelve un grafico boxplot por cada columna indicada
    en la lista"""

    fig, axes = plt.subplots(len(lista_col), 1, figsize=(30,20))

    axes = axes.flat

    for indice, columna in enumerate(lista_col):

        sns.boxplot(y = columna, data = dataframe, color = "purple", ax=axes[indice])
        axes[indice].set_title(columna)
        axes[indice].set_ylabel(columna)

        fig.tight_layout();


def eliminar_duplicados (dataframe):
    """Esta función elimina los duplicados generales de DataFrame y 
    mantiene la primera aparicion de los mismos
    
    Args:
    dataframe : DF al que queremos quitar duplicados
    
    Returns:
    La funcion no tiene return pero gracias al "inplace = True" devuelve el DataFrame 
    ya sin duplicados, ademas, devuelve varios prints de comprobacion"""
        
    print("Estos son los duplicados generales del DataFrame:")
    print(dataframe.duplicated().sum())
    dataframe.drop_duplicates(keep = "first", inplace = True)
    print("Duplicados eliminados")
    print("Comprobacion de la ausencia de duplicados")
    print(dataframe.duplicated().sum())

def union (dataframe1, dataframe2):

    """Esta función realiza un merge entre dos DataFrame, es decir, en
    el nuevo DF las columnas del segundo apareceran a la derecha de la del primero.
    La forma de hacer el merge es "left": debemos poner como DF1 el que queramos como base
    para buscar en el otro.
    En este caso la columna de union es "Loyalty Number"
    
    Args:
    dataframe1, dataframe2 : los dataframe que queremos unir
    
    Returns:
    La funcion devuelve el DataFrame ya sin duplicados y 
    varios prints de comprobacion"""

    merged_df = pd.merge(dataframe1, dataframe2, on="Loyalty Number", how='left')
    return merged_df