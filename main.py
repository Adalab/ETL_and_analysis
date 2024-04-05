#%%
import pandas as pd
from src import support_transformation as sp
#%%
df_flight_activity = pd.read_csv("files/Customer Flight Activity.csv")
df_loyalty_history = pd.read_csv("files/Customer Loyalty History.csv")

df_flight_activity.name = "Flight Activity"
df_loyalty_history.name = "Loyalty History"

lista_dfs = [df_flight_activity, df_loyalty_history]

# %%
sp.exploracion_general(lista_dfs)
sp.exploracion_columna(lista_dfs)
# %%
sp.graficos_boxp(df_flight_activity, ["Flights Booked", "Flights with Companions", "Total Flights"])
sp.graficos_hisp(df_loyalty_history, ["Gender", "Education", "Marital Status"])
# %%
df_flight_activity_notdup = sp.eliminar_duplicados(df_flight_activity)
# %%
df_total = sp.union(df_flight_activity, df_loyalty_history)