import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df=pd.read_csv("country_wise_latest.csv")
fig = px.choropleth(
    df,
    locations="Country/Region",
    locationmode="country names",
    color="Confirmed",
    hover_name="Country/Region",
    hover_data=["Confirmed", "Deaths", "Recovered"],
    color_continuous_scale="Reds",
    title="Mapa de Calor Global - Casos Confirmados de COVID-19"
)

fig.show()