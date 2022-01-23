from numpy import tile
import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")

#fig = px.line(df,x='Year',y='Per capita income',color="Country",title= 'Per capita income')
#fig = px.bar(df,x='Year',y='Per capita income',title= 'Per capita income')
fig = px.scatter(df,x="Population",y="Per capita",color="Country",title="Per capita income",size="Percentage"
,size_max=60
)

fig.show()