import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

dataUrl = 'https://query.data.world/s/oqk3vxvzb3ufpdoouxkfeysyjh6k5m'
title = '2020/W9: Sleep Hours Needed Vs. Averaged'
xLabel = 'SleepHours'
yLabel = 'Grades'

df = pd.read_excel(dataUrl)

print(df)
print(df[['Grade']])
print(df[['Hours Needed']])

#X
x1 = df.loc[:,'Grade']

#Y
y1 = df.loc[:,'Hours Averaged']
y2 = df.loc[:,'Hours Needed']

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=x1, y=y1,
                    mode='markers',
                    name='Hours Averaged'))
fig.add_trace(go.Scatter(x=x1, y=y2,
                    mode='markers',
                    name='Hours Needed'))

fig.update_layout(title=title,
                xaxis_title="Grades",
                yaxis_title="Hours")

fig.show()