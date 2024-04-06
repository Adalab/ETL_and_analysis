import mysql.connector



def creacion_bbdd (usuario, contrasenya, query):

    """Esta funcion crea un bbdd en mysql

    Args:
    - usuario: usuario para la conexion al servidor
    - contraseña: contraseña para la conexión al servidor
    - query: consulta SQL para la creacion de la bbdd

    Returns:
    No devuelve ningún valor
    """
    
    cnx = mysql.connector.connect(user=usuario, password=contrasenya,
                                host='127.0.0.1')


    mycursor = cnx.cursor()
    

    try: 
        mycursor.execute(query) 
    
        print("BBDD creada")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def creacion_tablas (usuario, contrasenya, bbdd, query):
    """Esta funcion crea una tabla en una bbdd en mysql

    Args:
    - usuario: usuario para la conexion al servidor
    - contraseña: contraseña para la conexión al servidor
    - bbdd: nombre de la bbdd donde queremos crear la tabla
    - query: Consulta SQL para la creacion de la tabla

    Returns:
    No devuelve ningún valor
    """
    cnx = mysql.connector.connect(user=usuario, password=contrasenya,
                                host='127.0.0.1', database= bbdd)


    mycursor = cnx.cursor()
    
    
    try: 
        mycursor.execute(query)
    
        print("Tabla empleado creada")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)

    cnx.close()

def insertar_datos(usuario, contrasenya, bbdd, query, lista_tuplas):
    """
    Esta funcion inserta datos en una tabla de una base de datos en mysql

    Args:
    - usuario: usuario para la conexion al servidor
    - contraseña: contraseña para la conexión al servidor
    - bbdd: nombre de la bbdd donde esta la tabla donde vamos a insertar datos
    - query: Consulta SQL para la insercion
    - lista_tuplas: lista que contiene las tuplas con los datos a insertar.

    Returns:
    No devuelve ningún valor
    """
    cnx = mysql.connector.connect(
        user=usuario, 
        password=contrasenya, 
        host="127.0.0.1", database=bbdd
    )

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, lista_tuplas)
        cnx.commit()
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()


def convertir_float(lista_tuplas):
    """
    Esta funcion convierte los elementos de una lista de tuplas a float cuando sea posible

    Args:
    - lista_tuplas: una lista que contiene tuplas 

    Returns:
    Devuelve una nueva lista con las mismas tuplas, pero con los elementos convertidos a float, cuando sea posible
    """
    datos_tabla_caract_def = []
    
    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(float(elemento))
            except:
                lista_intermedia.append(elemento)
            
        datos_tabla_caract_def.append(tuple(lista_intermedia))
    
    return datos_tabla_caract_def

def convertir_int(lista_tuplas):
    """
    Esta funcion convierte los elementos de una lista de tuplas a int cuando sea posible

    Args:
    - lista_tuplas: una lista que contiene tuplas 

    Returns:
    Devuelve una nueva lista con las mismas tuplas, pero con los elementos convertidos a int, cuando sea posible
    """
    datos_tabla_caract_def = []
    
    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(int(elemento))
            except:
                lista_intermedia.append(elemento)
            
        datos_tabla_caract_def.append(tuple(lista_intermedia))
    
    return datos_tabla_caract_def