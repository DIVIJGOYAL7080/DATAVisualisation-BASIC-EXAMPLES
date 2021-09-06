import pandas as  pd
import plotly.express as px
data=pd.read_csv("data.csv")
fig=px.bar(data,x="Country",y="Population",title="population servey")
fig.show()