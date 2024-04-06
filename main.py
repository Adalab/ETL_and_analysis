#%%
import pandas as pd
from src import support_transformation as sp
from src import support_conexion as cnx
from src import query_creacion as query
import warnings
warnings.filterwarnings("ignore")


#%%
df_flight_activity = pd.read_csv("files/Customer Flight Activity.csv")
df_loyalty_history = pd.read_csv("files/Customer Loyalty History.csv")

df_flight_activity.name = "Flight Activity"
df_loyalty_history.name = "Loyalty History"

# %%
lista_dfs = [df_flight_activity, df_loyalty_history]
sp.exploracion_general(lista_dfs)
sp.exploracion_columna(lista_dfs)

# %%
sp.graficos_boxp(df_flight_activity, ["Flights Booked", "Flights with Companions", "Total Flights"])
sp.graficos_boxp(df_loyalty_history, ["Salary", "CLV"])
sp.graficos_hisp(df_loyalty_history, ["Gender", "Education", "Marital Status"])

# %%
sp.cabeceras(lista_dfs)
sp.eliminar_duplicados(df_flight_activity)
sp.eliminar_negativos(df_loyalty_history, "salary")

# %%
df_total = sp.union(df_flight_activity, df_loyalty_history)

# %%
sp.exploracion_nulos(df_total)
# %%
lista = ["cancellation_year", "cancellation_month"]
df_total_notnull = sp.gestion_nulos(df_total, lista)

# %%
sp.exploracion_ceros(df_total_notnull)

# %%
sp.col_fecha(df_total_notnull, "year", "month", "year_month")
sp.col_fecha(df_total_notnull, "enrollment_year", "enrollment_month", "enrollment_year_month")
sp.col_fecha(df_total_notnull, "cancellation_year", "cancellation_month", "cancellation_year_month")
#%%
df_total_notnull.to_csv("files/df_final.csv")
# %%
cnx.creacion_bbdd("root", "AlumnaAdalab", query.query_creacion_bbdd)
cnx.creacion_tablas("root", "AlumnaAdalab", "Flights_Evaluacion_3", query.query_tabla_cliente)
cnx.creacion_tablas("root", "AlumnaAdalab", "Flights_Evaluacion_3", query.query_tabla_registros)
# %%
df_sin_duplicados = df_total_notnull.drop_duplicates(subset='loyalty_number')
# %%
datos_tabla_cliente = list(set(zip(df_sin_duplicados["loyalty_number"].values, df_sin_duplicados["country"].values, df_sin_duplicados["province"].values, df_sin_duplicados["city"].values, df_sin_duplicados["postal_code"].values, df_sin_duplicados["gender"].values, df_sin_duplicados["education"].values, df_sin_duplicados["salary"].values, df_sin_duplicados["marital_status"].values, df_sin_duplicados["loyalty_card"].values, df_sin_duplicados["clv"].values, df_sin_duplicados["enrollment_type"].values, df_sin_duplicados["enrollment_year"].values, df_sin_duplicados["enrollment_month"].values, df_sin_duplicados["cancellation_year"].values, df_sin_duplicados["cancellation_month"].values)))
datos_tabla_registros = list(set(zip(df_total_notnull["loyalty_number"].values, df_total_notnull["year"].values, df_total_notnull["month"].values, df_total_notnull["flights_booked"].values, df_total_notnull["flights_with_companions"].values, df_total_notnull["total_flights"].values, df_total_notnull["distance"].values, df_total_notnull["points_accumulated"].values, df_total_notnull["points_redeemed"].values, df_total_notnull["dollar_cost_points_redeemed"].values)))
#%%
datos_cliente = cnx.convertir_int(datos_tabla_cliente)
datos_cliente_f = cnx.convertir_float(datos_cliente)
datos_registros = cnx.convertir_int(datos_tabla_registros)
datos_registros_f = cnx.convertir_float(datos_registros)
#%%
cnx.insertar_datos("root", "AlumnaAdalab", "Flights_Evaluacion_3", query.query_insertar_cliente, datos_cliente_f)
# %%
cnx.insertar_datos("root", "AlumnaAdalab", "Flights_Evaluacion_3", query.query_insertar_registros, datos_registros_f)

