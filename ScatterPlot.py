import pandas as pd
import plotly.express as px

df = pd.read_csv("Data.csv")
fig = px.scatter(df, x="date", y="cases",
	            color="Country",
                size_max=60)
fig.show()
