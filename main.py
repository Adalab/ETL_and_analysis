#%%
import pandas as pd
from src import support_transformation as sp
import seaborn as sns
import matplotlib.pyplot as plt

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
sp.graficos_hisp(df_loyalty_history, ["Gender", "Education", "Marital Status"])

# %%
sp.cabeceras(lista_dfs)
df_flight_activity_notdup = sp.eliminar_duplicados(df_flight_activity)
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
