import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df=pd.read_csv("country_wise_latest.csv")
paises_com_mais_casos_recuperados=df.sort_values(by="Recovered",ascending=False).head(10)
paises_porcentagem = pd.DataFrame({
    'Porcentagem':  paises_com_mais_casos_recuperados['Recovered']*100 / paises_com_mais_casos_recuperados['Confirmed'],
    'Country/Region': paises_com_mais_casos_recuperados['Country/Region']
})

fig2 = px.bar(paises_porcentagem, x="Country/Region", y="Porcentagem", title="Países com Mais Casos Recuperados percentual", color="Country/Region")

fig2.show()