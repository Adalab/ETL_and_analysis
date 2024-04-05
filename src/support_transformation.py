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
            print(f"Frecuencia de valores en la columna: \n {dataframe[columna].value_counts()}")
            print(f"Suma de datos nulos {dataframe[columna].isnull().sum()}")
            print(f"Suma de datos duplicados {dataframe[columna].duplicated().sum()}")
            
def graficos_hisp (dataframe, lista_col):

    """Esta función crea graficos histplot para las columnas y el dataframe indicados
    
    Args:
    dataframe : DF que contiene las columnas que queremos analizar
    lista_col : lista de columnas que queremos analizar del DF anterior
    
    Returns:
    La funcion devuelve un grafico histplot por cada columna indicada
    en la lista"""

    fig, axes = plt.subplots(len(lista_col), 1, figsize=(10,5))

    axes = axes.flat

    for indice, columna in enumerate(lista_col):

        sns.histplot(x = columna, data = dataframe, color = "purple", kde = True, bins = 20, ax=axes[indice])
        axes[indice].set_title(columna)
        axes[indice].set_ylabel("Frecuencia")

        fig.tight_layout();

def graficos_boxp (dataframe, lista_col):

    """Esta función crea graficos boxplot para las columnas y el dataframe indicados
    
    Args:
    dataframe : DF que contiene las columnas que queremos analizar
    lista_col : lista de columnas que queremos analizar del DF anterior
    
    Returns:
    La funcion devuelve un grafico boxplot por cada columna indicada
    en la lista"""

    fig, axes = plt.subplots(len(lista_col), 1, figsize=(10,5))

    axes = axes.flat

    for indice, columna in enumerate(lista_col):

        sns.boxplot(x = columna, data = dataframe, color = "purple", ax=axes[indice])

        fig.tight_layout();

##FUNCIONES LIMPIEZA Y UNION##

def eliminar_duplicados (dataframe):
    """Esta función elimina los duplicados generales del DataFrame y 
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
    print("--------------------------------------------")

def union (dataframe1, dataframe2):

    """Esta función realiza un merge entre dos DataFrame, es decir, en
    el nuevo DF las columnas del segundo apareceran a la derecha de la del primero.
    La forma de hacer el merge es "left": debemos poner como DF1 el que queramos como base
    para buscar en el otro.
    En este caso la columna de union es "Loyalty Number"
    
    Args:
    dataframe1, dataframe2 : los dataframe que queremos unir
    
    Returns:
    La funcion devuelve un nuevo DataFrame unificado"""

    merged_df = pd.merge(dataframe1, dataframe2, on="loyalty_number", how='left')
    return merged_df

def cabeceras (lista):

    """Esta función renombra las cabeceras del DataFrame, sustituye espacios por "_"
    y las pone en minusculas.
    
    Args:
    lista : lista de DFs que queremos modificar
    
    Returns:
    La funcion no tiene return, modifica las cabeceras por asignacion directa"""

    for dataframe in lista:
        print("Modificamos DF {}".format(dataframe.name))
        dataframe.columns = [col.replace(" ", "_").lower() for col in dataframe.columns]
        print(f"Las nuevas cabeceras son: {dataframe.columns}")
        print("--------------------------------------------")

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

    
    for col in nulos_cat:
        print(f"La distribución de las categorías para la columna {col.upper()}")
        display(dataframe[col].value_counts() / dataframe.shape[0])
        print("........................")

    
    nulos_num = dataframe[dataframe.columns[dataframe.isnull().any()]].select_dtypes(include = np.number).columns
    print("Las columnas numéricas que tienen nulos son : \n ")
    print(nulos_num)
    print("........................")

    
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
    La funcion no tiene return, devuelve el DF modificado por asignacion directa"""    

    for columna in lista_unknown:
        dataframe[columna] = dataframe[columna].fillna("Unknown")
    print("Comprobacion de la ausencia de los nulos")
    print(dataframe[lista_unknown].isnull().sum())
    
    return dataframe


def exploracion_ceros (dataframe):

    """Esta función explora los ceros del DataFrame, nos mostrara el % de ceros de 
    las columnas numericas
    
    Args:
    dataframe : el dataframe que queremos explorar
    
    Returns:
    La funcion devuelve varios prints con la informacion obtenida"""


    col_con_ceros = []
    for col in dataframe:

        if dataframe[dataframe[col] == 0][col].count()> 0:
            col_con_ceros.append(col)

    print("Las columnas que tienen ceros son : \n ")
    print(col_con_ceros)
    print("........................")

    for colu in col_con_ceros:
        print(f"El porcentaje de ceros de la columna {colu} \n")
        print(dataframe[dataframe[colu] == 0][colu].count() / dataframe.shape[0])
        print("........................")



def eliminar_negativos (dataframe, columna):

    """Esta función sustituye los numeros negativos por np.nan
    
    Args:
    dataframe : el dataframe que queremos modificar
    
    Returns:
    La funcion no tiene return, devuelve el DF modificado por asignacion directa"""

    print(f"Estos son los datos negativos en {columna}")
    print(dataframe[dataframe[columna] < 0][columna])
    dataframe[columna] = dataframe[columna].apply(lambda dato : np.nan if dato < 0 else dato)
    print("Despues de establecer negativos como nulos")
    print(f"Estos son los datos negativos en {columna}")
    print("--------------------------------------------")

        

def col_fecha (dataframe, col1, col2, col_nueva):

    """Esta función crea 1 nueva columna de año/mes
    
    Args:
    dataframe : el dataframe que queremos modificar
    col1 : año o mes, segun el orden que queramos
    col2 : año o mes, segun el orden que queramos
    col_nueva : nombre que le vamos a dar a la nueva columna
    
    Returns:
    La funcion no tiene return, devuelve el DF modificado por asignacion directa"""

    dataframe[col_nueva] = dataframe.apply(lambda dato: str(dato[col1]) + "/" + str(dato[col2]), axis=1)

# %%
