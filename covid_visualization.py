import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df=pd.read_csv("country_wise_latest.csv")
paises_com_mais_casos=df.sort_values(by="Confirmed",ascending=False).head(10)
fig1 = px.bar(paises_com_mais_casos, x="Country/Region", y="Confirmed", title="Países com Mais Casos", color="Country/Region")
fig1.show()