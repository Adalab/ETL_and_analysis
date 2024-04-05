#%%
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

def cabeceras (dataframe):
    dataframe.columns = [col.replace(" ", "_").lower() for col in dataframe.columns]

def exploracion_nulos (dataframe):

    """Esta función explora los nulos del DataFrame, nos mostrara segun
    el tipo de columna (numerica o categorica) el % de nulos de cada una
    
    Args:
    dataframe : el dataframe que queremos explorar
    
    Returns:
    La funcion devuelve varios prints con la informacion obtenida"""
    
    nulos_cat = dataframe[dataframe.columns[dataframe.isnull().any()]].select_dtypes(include = "O").columns
    print("Las columnas categóricas que tienen nulos son : \n ")
    print(nulos_cat)
    print("........................")

    
    print("El porcentaje de nulos de cada una de las anteriores es: \n")
    print(dataframe[nulos_cat].isnull().sum() / dataframe.shape[0])
    print("........................")

    # % de nulos por categoria de cada columna
    for col in nulos_cat:
        print(f"La distribución de las categorías para la columna {col.upper()}")
        display(dataframe[col].value_counts() / dataframe.shape[0])
        print("........................")

    # sacamos una lista de las variables numericas que tienen nulos
    nulos_num = dataframe[dataframe.columns[dataframe.isnull().any()]].select_dtypes(include = np.number).columns
    print("Las columnas numéricas que tienen nulos son : \n ")
    print(nulos_num)
    print("........................")

    # nulos que tenemos en cada una de las columnas numericas
    print("El porcentaje de nulos de cada una de las anteriores es: \n")
    print(dataframe[nulos_num].isnull().sum() / dataframe.shape[0])

def gestion_nulos (dataframe, lista_unknown):

    """Esta función gestiona los nulos, en concreto para este Dataframe, 
    las columnas Cancellation Year y Cancellation Month son falsas numericas, 
    por lo que sustituiremos nulos por "Unknown" lo cual puede indicar o bien que
    no tenemos el dato o bien que sigue siendo cliente y no ha cancelado.
    
    Args:
    dataframe : el dataframe que queremos modificar
    
    Returns:
    La funcion devuelve el DF modificado"""    

    for columna in lista_unknown:
        dataframe[columna] = dataframe[columna].fillna("Unknown")
    print("Comprobacion de la ausencia de los nulos")
    print(dataframe[lista_unknown].isnull().sum())
    
    return dataframe
# %%
