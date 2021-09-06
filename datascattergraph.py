import pandas as  pd
import plotly.express as px
data=pd.read_csv("data.csv")
fig=px.scatter(data,x="Population",y="Per capita",color="Country",size="Percentage",size_max=60,title="population servey")
fig.show()